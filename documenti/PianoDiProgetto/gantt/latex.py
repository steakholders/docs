#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from utils import *

def writeGanttMilestone(project, milestone_id, filename):
	milestone = project.getMilestone(str(milestone_id))
	out = open(filename, "w")
	def latex(str):
		out.write((str+"\n").encode('utf-8'))

	latex(u"\\begin{{ganttchart}}{{{start}}}{{{end}}}".format(
		start = milestone.getStart(), end = milestone.getEnd()
	))
	latex(u"\t\\gantttitlecalendar{year, month=name, day} \\\\")
	
	for tasklist in sortByCode(milestone.getTaskLists()):
		latex(u"")
		latex(u"\t\\ganttgroup{{\\textbf{{{title}}}}}{{{start}}}{{{end}}} \\\\".format(
			title = tasklist.getFullName(), start = tasklist.getStart(), end = tasklist.getEnd()
		))

		tasks = sortByCode(tasklist.getTasks())
		
		for task in tasks:
			latex(u"\t\t\\ganttbar[name={id}]{{{title}}}{{{start}}}{{{end}}} \\\\".format(
				id = task.id, title = task.getFullName(), start = task.getStart(), end = task.getEnd()
			))
		
		for task in tasks:
			for dependency in task.getDependencies():
				latex(u"\t\t\\ganttlink{{{first}}}{{{second}}}".format(
					first = dependency.id, second = task.id
				))

	latex(u"\\end{ganttchart}")

	out.close()

def writeHoursTableMilestone(project, milestone_id, roles_id, filename):
	milestone = project.getMilestone(str(milestone_id))
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	tasks = milestone.getTasks()
	out = open(filename, "w")
	def latex(str):
		out.write((str+"\n").encode('utf-8'))

	for person in sortByName(milestone.getPeople()):
		latex(u"")
		latex(u"\t{name}".format(
			name = person.getName()
		))
		
		person_tasks = [t for t in tasks if t.getResponsible() == person]
		
		for role in roles:
			role_tasks = [t for t in person_tasks if t.getRole() == role]
			role_hours = sum([t.getPlannedHours() for t in role_tasks])

			latex(u" & {hours}".format(hours = role_hours))

		latex(u" \\\\")

	out.close()
