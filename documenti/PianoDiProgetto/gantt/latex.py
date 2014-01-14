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

def writeHoursTableMilestone(project, milestone_id, filename):
	milestone = project.getMilestone(str(milestone_id))
	out = open(filename, "w")
	def latex(str):
		out.write((str+"\n").encode('utf-8'))

	for tasklist in sortByCode(milestone.getTaskLists()):
		latex(u"")
		latex(u"\t\\textbf{{{code}}} & \\textbf{{{title}}} \\\\".format(
			code = tasklist.getCode(), title = tasklist.getName()
		))
		latex(u"\t\\cline{3-4}")
		
		tasks = sortByCode(tasklist.getTasks())
		
		for task in tasks:
			if task.role is not None:
				latex(u"\t{code} & {title} & {role} & {hours} \\\\".format(
					code = task.getCode(), title = task.getName(), role = task.role.name.title(), hours = task.getPlannedHours()
				))
			else:
				pedantic_warning(u"Il task {name} non ha un ruolo assegnato".format(name=task.getFullName()))
				latex(u"\t{code} & {title} & {role} & {hours} \\\\".format(
					code = task.getCode(), title = task.getName(), role = "(da assegnare)", hours = task.getPlannedHours()
				))

		latex(u"\t\\hline")

	out.close()

