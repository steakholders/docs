#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import re
from datetime import date, datetime, timedelta
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

def date_parse(str):
	return datetime.strptime(str, "%Y%m%d").date()
	#return datetime.strptime(str, "%Y-%m-%dT%H:%M:%S")

def take_brackets(str):
	matches = re.findall(r"(\(\s*\w+\s*\))", str)
	matches = [x for x in matches]
	
	if len(matches) == 0:
		return (str, None)

	token = matches[-1]
	str = str.replace(token, "")
	content = token.strip('()').strip().lower()
	
	return (str, content)


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

		self.project.addPerson(self.id, self)

	def __repr__(self):
		return u"<Person(#{id} {name})>".format(id=self.id, name=self.name).encode('utf-8')

class Role:
	def __init__(self, project, name, hour_cost):
		self.project = project
		self.name = name
		self.hour_cost = hour_cost

	def __repr__(self):
		return u"<Role({name})>".format(name=self.name).encode('utf-8')

class TimeEntry:
	def __init__(self, project, task, id, minutes):
		self.project = project
		self.task = task
		self.id = id
		self.minutes = minutes

		self.task.addTime(self)

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

		self.project.addTask(self.id, self)
		self.tasklist.addTask(self.id, self)

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
			new_name, role_token = take_brackets(self.name)
			print self.name, new_name, role_token

			# Se è tra i ruoli riconosciuti
			if role_token in self.project.roles:
				# Recupera il ruolo
				self.role = self.project.roles[role_token]
				self.name = new_name

			if role_token is "extra":
				# Il tempo extra non deve essere conteggiato
				self.hours = 0
				self.role = None
				self.name = new_name

		if self.role == None:
			warning(u"Non è stato assegnato un ruolo al task {nome}".format(nome=self.name))

	def getDays(self):
		return (self.end - self.start + timedelta(days=1)).days

	def addDependency(self, dependency_id):
		try:
			dependency = self.project.tasks[dependency_id]

			self.dependencies.update({
				dependency_id: dependency
			})
		except KeyError as key:
			pedantic_warning(u"Il task '{name}'' dipende dal task {dep} che nell'elenco viene dopo".format(
				name=self.name,
				dep=tasklist.name
			))

	def addTime(self, time):
		

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
		self.time = {}

	def load(self):
		self.initRoles()
		self.initPeople()
		self.initTime()
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

				for dependency in task["predecessors"]:
					if dependency["type"] == "start":
						new_task.addDependency(dependency["id"])
						

	def addPerson(self, person_id, person):
		self.people.update({
			person_id: person
		})

	def initPeople(self):
		tw = Factory.createTeamworkClient(self.company)
		data = tw.requestJSON("/projects/{project_id}/people".format(project_id=self.id))

		for person in data["people"]:
			Factory.createPerson(self, person["id"], person["first-name"]+" "+person["last-name"])

	def addTime(self, timeentry):
		pass

	def initTime(self):
		tw = Factory.createTeamworkClient(self.company)
		self.time = {}
		page = 0
		while True:
			page += 1
			data = tw.requestJSON("/projects/{project_id}/time_entries".format(project_id=self.id), "page={page}".format(page=page))

			if len(data["time_entries"]) == 0:
				break

			for time in data["time_entries"]:
				# TODO
				self.addTime(time)
	
		for person in data["people"]:
			Factory.createPerson(self, person["id"], person["first-name"]+" "+person["last-name"])

	def getTasks(self, milestones_id=None):
		if milestones is None:
			return self.tasks.values()

		# Restituisci i task che sono in una lista che ha una milestone tra milestones_id
		lists = [x for x in self.tasks.values() if x.milestone.id in milestones_id]

		tasks = []
		for x in lists.getTasks():
			tasks.append(x)
		return tasks

	def getPeople(self):
		return self.people.values()

	def getRoles(self):
		return self.roles.values()


