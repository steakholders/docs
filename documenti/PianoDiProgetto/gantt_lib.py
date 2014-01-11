#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2, base64
import json
from os import path
from pprint import pprint

class GanttException(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return "/!\\ ERROR: "+self.message

def warning(message):
	print "/!\\ ATTENZIONE: "+message


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
		self.name = name.encode("utf8")

	def __repr__(self):
		return "<Person(#{id} {name})>".format(id=self.id, name=self.name)

class Role:
	def __init__(self, project, name, hour_cost):
		self.project = project
		self.name = name
		self.hour_cost = hour_cost

class Task:
	def __init__(self, project, id, start, end, name, responsible=None):
		self.project = project
		self.id = id
		self.start = start
		self.end = end
		self.name = name
		self.dependencies = {}
		self.responsible = responsible

	def addDependency(self, dependency_id, dependency):
		self.dependencies.update({
			dependency_id: dependency
		})

class TaskList:
	def __init__(self, project, id, name, milestone=None):
		self.project = project
		self.id = id
		self.name = name
		self.tasks = {}

	def addTask(self, task_id, task):
		self.tasks.update({
			task_id: task
		})

class Milestone:
	def __init__(self, project, id, deadline, name):
		self.project = project
		self.id = id
		self.deadline = deadline
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
			"responsabile": Factory.createRole(self, "responsabile", 30),
			"analista": Factory.createRole(self, "analista", 25),
			"amministratore": Factory.createRole(self, "amministratore", 20),
			"progettista": Factory.createRole(self, "progettista", 22),
			"verificatore": Factory.createRole(self, "verificatore", 15),
			"programatore": Factory.createRole(self, "programatore", 15)
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
		data = tw.requestJSON("/projects/{project_id}/todo_lists".format(project_id=self.id))
		
		for tasklist in data["todo-lists"]:
			milestone = None
			if len(tasklist["milestone-id"])> 0:
				milestone = self.milestones[tasklist["milestone-id"]]

			new_tasklist = Factory.createTaskList(self, tasklist["id"], tasklist["name"], milestone)
			self.addTaskList(tasklist["id"], new_tasklist)

			for task in tasklist["todo-items"]:
				responsible = None
				if "responsible-party-ids" in task:
					responsible_ids = task["responsible-party-ids"].split(",")
					
					if len(responsible_ids) > 1:
						raise GanttException('È stato assegnato più di una persona ({responsibles}) al task "{task_name}"'.format(
							responsibles = ", ".join([self.people[id].name for id in responsible_ids]),
							task_name = task["content"]
						))
					
					if len(responsible_ids) == 1:
						responsible = self.people[responsible_ids[0]]
					
				new_task = Factory.createTask(self, task["id"], task["start-date"], task["due-date"], task["content"], responsible)
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
			self.key = raw_input("Inserire la chiave privata per le API di TeamworkPM del tuo utente: ")	

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
