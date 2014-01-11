#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gantt_lib import Factory, warning, pedantic_warning, error

MIN_HOURS = 95
MAX_HOURS = 105
MAX_HOURS_PER_DAY = 3

def printProjectReport(project):
	print
	print "Riepilogo progetto"
	print "------------------"
	print "Milestone: {num}".format(num=len(project.milestones))
	print "Persone: {num}".format(num=len(project.people))
	print "Ruoli: {num}".format(num=len(project.roles))
	print "TaskList: {num}".format(num=len(project.tasklists))
	print "Task: {num}".format(num=len(project.tasks))

def printTaskLists(project):
	print
	print "Liste"
	print "-----"
	for l in project.tasklists.values():
		print "* {nome} da {start} a {end}: {num} task".format(
			nome = l.name,
			start = l.getStart(),
			end = l.getEnd(),
			num = len(l.tasks)
		)

def testMaxWorkHoursPerDay(project):
	print
	print "testMaxWorkHoursPerDay"
	print "----------------------"
	for task in project.getTasks():
		# Avvisa se ci sono più di MAX_HOURS_PER_DAY ore per giorno
		if task.hours > (task.end - task.start).days * MAX_HOURS_PER_DAY:
			warning(u'Al task "{name}" sono state assegnate troppe ore ({hours}, {max_hours})'.format(
				name = self.name,
				hours = self.hours,
				max_hours = (self.end - self.start).days * MAX_HOURS_PER_DAY
			))

def testMinMaxWorkHours(project):
	print
	print "testMinMaxWorkHours"
	print "-------------------"
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		hours = sum([t.hours for t in tasks])
		print "- {nome} fa in tutto {hours} di lavoro".format(nome=person, hours=hours)


project = Factory.createProject("steakholders", id=65465)
project.load()

printProjectReport(project)
printTaskLists(project)

testMaxWorkHoursPerDay(project)
testMinMaxWorkHours(project)

