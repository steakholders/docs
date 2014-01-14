#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import re
from datetime import date, datetime, timedelta
from pprint import pprint
from client import TeamworkPMClient
from utils import *
from schema import *

def date_parse(str):
	return datetime.strptime(str, "%Y%m%d").date()

def datetime_parse(str):
	return datetime.strptime(str, "%Y-%m-%dT%H:%M:%SZ")

def take_brackets(str):
	matches = re.findall(r"(\(\s*\w+\s*\))", str)
	matches = [x for x in matches]
	
	if len(matches) == 0:
		return (str, None)

	token = matches[-1]
	str = str.replace(token, "")
	content = token.strip('()').strip().lower()
	
	return (str, content)

def split_code_name(title):
	array = title.split("-", 1)

	if len(array) > 1:
		return (array[0].strip(), array[1].strip())
	else:
		return (None, title)


class GanttException(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return "ERRORE: "+self.message.encode('utf-8')


class TeamworkPMDownload(TeamworkPMClient):
	def __init__(self, company="steakholders", key=None):
		TeamworkPMClient.__init__(self, company=company, key=key)

	def getMilestones(self, project):
		data = self.requestJSON("/projects/{project_id}/milestones".format(project_id=project.id), "find=all")
		
		for milestone in data["milestones"]:
			milestone_oby = Milestone(project, milestone["id"], date_parse(milestone["deadline"]), milestone["title"])
			project.addMilestone(milestone_oby)

	def getPeople(self, project):
		data = self.requestJSON("/projects/{project_id}/people".format(project_id=project.id))

		for person in data["people"]:
			person_obj = Person(project, person["id"], person["first-name"]+" "+person["last-name"])
			project.addPerson(person_obj)

	def getTaskLists(self, project):
		data = self.requestJSON("/projects/{project_id}/todo_lists".format(project_id=project.id), "status=all")
		
		for tasklist in data["todo-lists"]:

			# Ignora le TaskList senza milestone
			if len(tasklist["milestone-id"]) == 0:
				continue
			
			milestone = project.getMilestone(tasklist["milestone-id"])

			(tasklist_code, tasklist_name) = split_code_name(tasklist["name"])

			if tasklist_code is None:
				raise GanttException(u'Alla task-list #{id} "{name}" manca il codice identificativo. Me lo aspetto nel formato "XY1 - Titolo esteso"'.format(
					id = tasklist["id"],
					name = tasklist["name"],
				))
			
			tasklist_obj = TaskList(milestone, tasklist["id"], tasklist_code, tasklist_name)
			milestone.addTaskList(tasklist_obj)

			for task in tasklist["todo-items"]:
				responsible_id = None
				if "responsible-party-ids" in task:
					responsible_ids = task["responsible-party-ids"].split(",")
					
					if len(responsible_ids) > 1:
						raise GanttException(u'È stato assegnato più di una persona ({num}) al task "{task_name}", lista "{tasklist_name}"'.format(
							num = len(responsible_ids),
							task_name = task["content"],
							tasklist_name = tasklist_obj.getFullName()
						))
					
					if len(responsible_ids) == 1:
						responsible_id = responsible_ids[0]

				planned_hours = None
				if len(task['estimated-minutes']) > 0:
					estimated_minutes = int(task['estimated-minutes'])
					if estimated_minutes > 0:
						planned_hours = estimated_minutes/60

				# Leggi il nome del ruolo
				task_name = task["content"]
				partial_title, role = take_brackets(task_name)
				role_obj = project.getRole(role)
				if role_obj is not None:
					task_name = partial_title

				(code, task_name) = split_code_name(task_name)

				if code is None:
					raise GanttException(u'Al task #{id} "{task_name}" manca il codice identificativo. Me lo aspetto nel formato "XY1.2.3 - Titolo esteso (ruolo)"'.format(
						id = task["id"],
						task_name = task["content"],
					))
				
				task_obj = Task(
					tasklist_obj, task["id"], date_parse(task["start-date"]), date_parse(task["due-date"]), code, task_name,
					responsible = project.getPerson(responsible_id), role = role_obj, planned_hours = planned_hours
				)
				tasklist_obj.addTask(task_obj)

				for dependency in task["predecessors"]:
					if dependency["type"] == "start":
						task_obj.addDependency(project.getTask(dependency["id"]))

	
	def getTimeEntries(self, project):
		page = 0
		while True:
			page += 1
			data = self.requestJSON("/projects/{project_id}/time_entries".format(project_id=project.id), "page={page}".format(page=page))

			if len(data["time-entries"]) == 0:
				break

			for timeentry in data["time-entries"]:
				task = project.getTask(timeentry["todo-item-id"])
				hours = int(timeentry["hours"]) + int(timeentry["minutes"])/60
				timeentry_obj = TimeEntry(
					task,
					timeentry["id"],
					timeentry["description"],
					datetime = datetime_parse(timeentry["date"]),
					description = timeentry["description"]
				)
				
				if task is None:
					pedantic_warning(u'La TimeEntry #{id} è assegnata ad un task sconosciuto ({task})'.format(
						id = timeentry_obj.id, task = timeentry["todo-item-id"]
					))
					continue
				
				if task is None:
					pedantic_warning(u'La TimeEntry #{id} è assegnata ad una persona che non è responsabile del task "{name}" a cui è associata'.format(
						id = timeentry_obj.id, name = task.getFullName()
					))
					continue
				
				task.addTimeEntry(time)
	