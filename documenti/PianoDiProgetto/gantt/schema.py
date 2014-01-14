#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from datetime import timedelta
from parametri import *
from utils import *


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


class TimeEntry:
	def __init__(self, task, id, hours, description="", datetime=None):
		self.task = task
		self.id = id
		self.hours = hours
		self.description = description
		self.datetime = datetime

	def getWorkHours(self):
		return self.hours


class Task:
	def __init__(self, tasklist, id, start, end, code, name, responsible=None, role=None, planned_hours=None):
		self.tasklist = tasklist
		self.id = id
		self.start = start
		self.end = end
		self.code = code
		self.name = name
		self.responsible = responsible
		self.role = role
		self.planned_hours = planned_hours
		
		self.dependencies = {}
		self.timeentries = {}

		# Avvisa che non è stato assegnato
		if self.responsible is None:
			pedantic_warning(u'Non è stato assegnato nessuno al task "{name}"'.format(name = self.getFullName()))
		
		if self.role is None:
			pedantic_warning(u"Non è stato assegnato nessun ruolo al task {nome}".format(nome=self.getFullName()))

	def getFullName(self):
		return self.code + " - " + self.name
	
	def getName(self):
		return self.name
	
	def getCode(self):
		return self.code
	
	def getDays(self):
		return (self.end - self.start + timedelta(days=1)).days

	def getStart(self):
		return self.start
	
	def getEnd(self):
		return self.end

	def getPlannedHours(self):
		if self.planned_hours is None:
			return self.getDays() * DEFAULT_HOURS_PER_DAY
		else:
			return self.planned_hours

	def getWorkHours(self):
		if len(self.timeentries) > 0:
			return sum([x.getWorkHours() for x in self.timeentries])
		else:
			return self.getPlannedHours()

	def addDependency(self, dependency):
		self.dependencies.update({
			dependency.id: dependency
		})

	def getDependencies(self):
		return self.dependencies.values()

	def addTimeEntry(self, timeentry):
		self.timeentries.update({
			time.id: time
		})

	def getTimeEntry(self, timeentry_id):
		if timeentry_id not in self.tasks:
			return None

		return self.timeentries[timeentry_id]

	def getTimeEntries(self):
		return self.timeentries.values()


class TaskList:
	def __init__(self, milestone, id, code, name):
		self.milestone = milestone
		self.id = id
		self.code = code
		self.name = name
		self.tasks = {}
		
	def getFullName(self):
		return self.code + " - " + self.name
	
	def getName(self):
		return self.name
	
	def getCode(self):
		return self.code
	
	def addTask(self, task):
		self.tasks.update({
			task.id: task
		})

	def getTask(self, task_id):
		if task_id not in self.tasks:
			return None

		return self.tasks[task_id]
	
	def getTasks(self):
		return self.tasks.values()
	
	def getStart(self):
		if len(self.tasks) == 0:
			return None
		
		return min([x.start for x in self.tasks.values()])

	def getEnd(self):
		if len(self.tasks) == 0:
			return None

		return max([x.end for x in self.tasks.values()])


class Milestone:
	def __init__(self, project, id, deadline, name):
		self.project = project
		self.id = id
		self.deadline = deadline
		self.name = name
		self.tasklists = {}

	def addTaskList(self, tasklist):
		self.tasklists.update({
			tasklist.id: tasklist
		})

	def getTaskList(self, tasklist_id):
		if tasklist_id not in self.tasklists:
			return None
		
		return self.tasklists[tasklist_id]		
	
	def getTaskLists(self):
		return self.tasklists.values()

	def getTask(self, task_id):
		for t in self.getTaskLists():
			task = t.getTask(task_id)
			if task is not None:
				return task
		return None

	def getTasks(self):
		tasks = []
		for t in self.getTaskLists():
			tasks.extend(t.getTasks())
		return tasks

	def getEnd(self):
		if len(self.tasklists) == 0:
			return self.deadline

		return max([x.getEnd() for x in self.tasklists.values()]+[self.deadline])

	def getStart(self):
		if len(self.tasklists) == 0:
			return None
		
		return min([x.getStart() for x in self.tasklists.values()])


class Project:
	def __init__(self, id):
		self.id = id
		self.milestones = {}
		self.people = {}
		self.roles = {}

		self.initRoles()

	# Role
	def initRoles(self):
		self.roles = {
			u"responsabile": Role(self, u"responsabile", 30),
			u"analista": Role(self, u"analista", 25),
			u"amministratore": Role(self, u"amministratore", 20),
			u"progettista": Role(self, u"progettista", 22),
			u"verificatore": Role(self, u"verificatore", 15),
			u"programmatore": Role(self, u"programatore", 15)
		}

	def getRole(self, role_name):
		if role_name in self.roles:
			return self.roles[role_name]

		return None
		
	def getRoles(self):
		return self.roles.values()
	
	# Milestone
	def addMilestone(self, milestone):
		self.milestones.update({
			milestone.id: milestone
		})

	def getMilestone(self, milestone_id):
		if milestone_id not in self.milestones:
			return None
		
		return self.milestones[milestone_id]

	def getMilestones(self):
		return self.milestones.values()

	# People
	def addPerson(self, person):
		self.people.update({
			person.id: person
		})
		
	def getPerson(self, person_id):
		if person_id not in self.people:
			return None
		
		return self.people[person_id]
		
	def getPeople(self):
		return self.people.values()

	# TaskLists
	def getTaskLists(self):
		tasklists = []
		for m in self.getMilestones():
			tasklists.extend(m.getTaskLists())
		return tasklists

	# Tasks
	def getTask(self, task_id):
		for m in self.getMilestones():
			task = m.getTask(task_id)
			if task is not None:
				return task
		return None

	def getTasks(self):
		tasks = []
		for m in self.getMilestones():
			tasks.extend(m.getTasks())
		return tasks
