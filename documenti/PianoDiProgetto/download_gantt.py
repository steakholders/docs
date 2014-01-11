#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2, base64
import json
from os import path
from pprint import pprint

class Task:
	def __init__(self, start, end, title, predecessors=[]):
		self.start = start
		self.end = end
		self.title = title
		self.predecessors = predecessors

class TaskList:
	def __init__(self, title):
		self.title = title

class Milestone:
	def __init__(self, date, title):
		self.date = date
		self.title = title

class Gantt:
	def __init__(self):
		self.milestones = []

	def createMilestone(self, *args, **kwargs):
		m = Milestone(*args, **kwargs)
		self.milestones.append(m)
		return m

	def createTaskList(self, *args, **kwargs):
		return TaskList(*args, **kwargs)

	def createTask(self, *args, **kwargs):
		return TaskList(*args, **kwargs)


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
			except IOError as e:
				while self.key is None or len(self.key) == 0:
					self.key = raw_input("Inserire la chiave privata per le API di TeamworkPM del tuo utente: ")	
		else:
			self.key = key

		# Salva la chiave privata nella home (in chiaro!)
		out_file = open(self.private_key_file, "w")
		json.dump(key, out_file)
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

	def getTaskList(self, project_id, parameters=""):
		return self.requestJSON("projects/{project_id}/todo_lists".format(project_id=project_id), parameters)


##########
#  Main  #
##########

tw = TeamworkPMClient("steakholders")
pprint(tw.getTaskList(project_id=65465))