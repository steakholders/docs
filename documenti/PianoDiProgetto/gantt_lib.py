#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import re
from dateutil.parser import parse as date_parse
from datetime import date
import urllib2, base64
import json
from os import path
from pprint import pprint

DEFAULT_HOURS_PER_DAY = 2

class GanttException(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return "ERRORE: "+self.message.encode('utf-8')

def warning(message):
	print "ATTENZIONE: "+message.encode('utf-8')

def pedantic_warning(message):
	disable = True
	if disable: return
	print "ATTENZIONE: "+message.encode('utf-8')


class Factory:
	singleton_tw_client = None

	@staticmethod
	def createTeamworkClient(*args, **kwargs):
		if Factory.singleton_tw_client is None:
			Factory.singleton_tw_client = TeamworkPMClient(*args, **kwargs)
		return Factory.singleton_tw_client
	
	@staticmethod
	def createProject(*args, **kwargs):
		return Project(*args, **kwargs)
	
	@staticmethod
	def createRole(*args, **kwargs):
		return Role(*args, **kwargs)

	@staticmethod
	def createMilestone(*args, **kwargs):
		return Milestone(*args, **kwargs)

	@staticmethod
	def createTaskList(*args, **kwargs):
		return TaskList(*args, **kwargs)

	@staticmethod
	def createTask(*args, **kwargs):
		return Task(*args, **kwargs)

	@staticmethod
	def createPerson(*args, **kwargs):
		return Person(*args, **kwargs)



class Person:
	def __init__(self, project, id, name):
		self.project = project
		self.id = id
		self.name = name

	def __repr__(self):
		return u"<Person(#{id} {name})>".format(id=self.id, name=self.name).encode('utf-8')

class Role:
	def __init__(self, project, name, hour_cost):
		self.project = project
		self.name = name
		self.hour_cost = hour_cost

	def __repr__(self):
		return u"<Role({name})>".format(name=self.name).encode('utf-8')

class Task:
	def __init__(self, project, tasklist, id, start, end, name, responsible=None, role=None, hours=None):
		self.project = project
		self.tasklist = tasklist
		self.id = id
		self.start = date_parse(start)
		self.end = date_parse(end)
		self.name = name
		self.dependencies = {}
		self.responsible = responsible
		self.role = role
		self.hours = hours

		# Recupera il riferimento al responsabile
		if isinstance(self.responsible, basestring):
			self.responsible = self.project.people[self.responsible]

		# Avvisa che non è stato assegnato
		if self.responsible == None:
			pedantic_warning(u'Non è stato assegnato nessuno al task "{name}"'.format(name = self.name))
		
		# Assegna di default DEFAULT_HOURS_PER_DAY di ore per giorno
		if self.hours == None:
			self.hours = (self.end - self.start).days * DEFAULT_HOURS_PER_DAY
			pedantic_warning(u'Non è stato assegnato un tempo al task "{name}", assumo che richieda {hours} ore'.format(
				name = self.name,
				hours = self.hours
			))

		# Recupera il riferimento al ruolo
		if isinstance(self.role, basestring):
			self.role = self.project.roles[self.role]
		
		# Se non è stato specificato un ruolo, recupera il ruolo dal nome
		if self.role == None:
			matches = re.findall(r"\((\s*\w+\s*)\)", self.name)
			matches = [x.strip().lower() for x in matches]
			
			# Per ogni elemento trovato tra parentesi, partendo dall'ultimo
			for role_token in matches[::-1]:
				# Se è tra i ruoli riconosciuti
				if role_token in self.project.roles:
					# Recupera il ruolo ed esci dal ciclo for
					self.role = self.project.roles[role_token]
					break

		if self.role == None:
			warning(u"Non è stato assegnato un ruolo al task {nome}".format(nome=self.name))

	def addDependency(self, dependency_id, dependency):
		self.dependencies.update({
			dependency_id: dependency
		})

class TaskList:
	def __init__(self, project, id, name, milestone):
		self.project = project
		self.id = id
		self.name = name
		self.tasks = {}
		self.milestone = milestone

		if isinstance(self.milestone, basestring):
			self.milestone = self.project.milestones[self.milestone]
		
	def addTask(self, task_id, task):
		self.tasks.update({
			task_id: task
		})

	def getEnd(self):
		if len(self.tasks) == 0:
			return None

		return max([x.end for x in self.tasks.values()])

	def getStart(self):
		if len(self.tasks) == 0:
			return None
		
		return min([x.start for x in self.tasks.values()])

class Milestone:
	def __init__(self, project, id, deadline, name):
		self.project = project
		self.id = id
		self.deadline = date_parse(deadline)
		self.name = name

class Project:
	def __init__(self, company, id):
		self.company = company
		self.id = id
		self.milestones = {}
		self.tasklists = {}
		self.tasks = {}
		self.people = {}
		self.roles = {}

	def load(self):
		self.initRoles()
		self.initPeople()
		self.initMilestones()
		self.initTaskLists()

	def initRoles(self):
		self.roles = {
			u"responsabile": Factory.createRole(self, u"responsabile", 30),
			u"analista": Factory.createRole(self, u"analista", 25),
			u"amministratore": Factory.createRole(self, u"amministratore", 20),
			u"progettista": Factory.createRole(self, u"progettista", 22),
			u"verificatore": Factory.createRole(self, u"verificatore", 15),
			u"programmatore": Factory.createRole(self, u"programatore", 15)
		}

	def addMilestone(self, milestone_id, milestone):
		self.milestones.update({
			milestone_id: milestone
		})

	def initMilestones(self):
		tw = Factory.createTeamworkClient(self.company)
		data = tw.requestJSON("milestones")

		for milestone in data["milestones"]:
			self.addMilestone(milestone["id"], Factory.createMilestone(self, milestone["id"], milestone["deadline"], milestone["title"]))

	def addTaskList(self, tasklist_id, tasklist):
		self.tasklists.update({
			tasklist_id: tasklist
		})
	
	def addTask(self, task_id, task):
		self.tasks.update({
			task_id: task
		})

	def initTaskLists(self):
		tw = Factory.createTeamworkClient(self.company)
		data = tw.requestJSON("/projects/{project_id}/todo_lists".format(project_id=self.id), "status=all")
		
		for tasklist in data["todo-lists"]:

			# Ignora le TaskList senza milestone
			if len(tasklist["milestone-id"]) == 0:
				continue
			
			new_tasklist = Factory.createTaskList(self, tasklist["id"], tasklist["name"], tasklist["milestone-id"])
			self.addTaskList(tasklist["id"], new_tasklist)

			for task in tasklist["todo-items"]:
				responsible_id = None
				if "responsible-party-ids" in task:
					responsible_ids = task["responsible-party-ids"].split(",")
					
					if len(responsible_ids) > 1:
						raise GanttException(u'È stato assegnato più di una persona ({responsibles}) al task "{task_name}", lista "{tasklist_name}"'.format(
							responsibles = ", ".join([self.people[id].name for id in responsible_ids]),
							task_name = task["content"],
							tasklist_name = tasklist["name"]
						))
					
					if len(responsible_ids) == 1:
						responsible_id = responsible_ids[0]

				# Leggi la durata stimata (se c'è, altrimenti il task internamente assumerà DEFAULT_HOURS_PER_DAY ore al giorno)
				hours = None
				if len(task['estimated-minutes']) > 0:
					estimated_minutes = int(task['estimated-minutes'])
					if estimated_minutes > 0:
						hours = estimated_minutes/60

				new_task = Factory.createTask(self, new_tasklist, task["id"], task["start-date"], task["due-date"], task["content"], responsible=responsible_id, hours=hours)
				self.addTask(task["id"], new_task)
				new_tasklist.addTask(task["id"], new_task)

				for dependency in task["predecessors"]:
					if dependency["type"] == "start":
						new_task.addDependency(dependency["id"], self.tasks[dependency["id"]])

				

	def addPerson(self, person_id, person):
		self.people.update({
			person_id: person
		})

	def initPeople(self):
		tw = Factory.createTeamworkClient(self.company)
		data = tw.requestJSON("/projects/{project_id}/people".format(project_id=self.id))

		for person in data["people"]:
			self.addPerson(person["id"], Factory.createPerson(self, person["id"], person["first-name"]+" "+person["last-name"]))

	def getTasks(self):
		return self.tasks.values()

	def getPeople(self):
		return self.people.values()

	def getRoles(self):
		return self.roles.values()


class TeamworkPMClient:
	def __init__(self, company="steakholders", key=None):
		self.company = company
		self.private_key_file = path.expanduser("~/.teamworkpm_private_key")
		self.key = ""
		
		# Ottieni la chiave privata
		if key is None or len(key) == 0:
			try:
				in_file = open(self.private_key_file, "r")
				self.key = json.load(in_file)
				in_file.close()
			except IOError:
				pass
		else:
			self.key = key
		
		# Chiedila se è vuota
		while self.key is None or len(self.key) == 0:
			self.key = raw_input(u"Inserisci la chiave privata per le API di TeamworkPM del tuo utente: ")	

		# Salva la chiave privata nella home (in chiaro!)
		out_file = open(self.private_key_file, "w")
		json.dump(self.key, out_file)
		out_file.close()

	def request(self, action):
		request = urllib2.Request("https://{0}.teamworkpm.net/{1}".format(self.company, action))
		request.add_header("Authorization", "BASIC " + base64.b64encode(self.key + ":xxx"))
		response = urllib2.urlopen(request)
		data = response.read()
		return data

	def requestJSON(self, base_action, parameters=""):
		action = base_action+".json"
		if len(parameters) > 0:
			action += "?" + parameters

		json_data = self.request(action)
		data = json.loads(json_data)
		return data
