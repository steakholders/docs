#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from utils import *

def writeGanttMilestone(project, milestone_id, filename):
	milestone = project.getMilestone(str(milestone_id))

	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

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

def writeRipartizioneOre(project, milestone_ids, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]

	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	tasklists = joinLists([m.getTaskLists() for m in milestones])
	for tasklist in sortByCode(tasklists):
		latex(u"")
		latex(u"\t\\textbf{{{code}}} & \\textbf{{{title}}} \\\\".format(
			code = tasklist.getCode(), title = tasklist.getName()
		))
		
		tasks = sortByCode(tasklist.getTasks())
		
		for task in tasks:
			if task.role is not None:
				latex(u"\t{code} & {title} & {role} & {hours:.0f} \\\\".format(
					code = task.getCode(), title = task.getName(), role = task.role.name.title(), hours = task.getPlannedHours()
				))
			else:
				pedantic_warning(u"Il task {name} non ha un ruolo assegnato".format(name=task.getFullName()))
				latex(u"\t{code} & {title} & {role} & {hours:.0f} \\\\".format(
					code = task.getCode(), title = task.getName(), role = "(non assegnato)", hours = task.getPlannedHours()
				))

		latex(u"\t\\hline")

	out.close()

def writeSuddivisioneOre(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	for person in sortByName(project.getPeople()):
		person_planned_hours = 0
		
		latex(u"\t{name}".format(name = person.getName()), False)
		
		for role in roles:
			planned_hours = sum([m.getPersonRoleCost(person, role).getPlannedHours() for m in milestones])
			person_planned_hours += planned_hours
			
			latex(u" & {hours:.0f}".format(hours = planned_hours), False)
		
		latex(u" & {hours:.0f}".format(hours = person_planned_hours), False)

		latex(u" \\\\")

	out.close()

def writeProspetto(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	planned_total_cost = 0
	planned_total_hours = 0
	for role in roles:
		role_costs = joinLists([
			[milestone.getPersonRoleCost(person, role) for person in project.getPeople()]
			for milestone in milestones
		])
		
		planned_cost = sum([c.getPlannedCost() for c in role_costs])
		planned_hours = sum([c.getPlannedHours() for c in role_costs])
		planned_total_cost += planned_cost
		planned_total_hours += planned_hours

		latex(u"\t{name} & {hours:.0f} & {cost:.0f} € \\\\".format(
			name = role.getName().title(),
			hours = planned_hours,
			cost = planned_cost
		))
	
	latex(u"\\hline")
	latex(u"\tTotale & {hours:.0f} & {cost:.0f} € \\\\".format(
		hours = planned_total_hours,
		cost = planned_total_cost
	))
	latex(u"\\hline")
	
	out.close()

def writeConsuntivoComponent(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	for person in sortByName(project.getPeople()):
		person_planned_hours = 0
		person_work_hours = 0
		
		latex(u"\t{name}".format(name = person.getName()), False)
		
		for role in roles:
			planned_hours = sum([m.getPersonRoleCost(person, role).getPlannedHours() for m in milestones])
			work_hours = sum([m.getPersonRoleCost(person, role).getWorkHours() for m in milestones])
			person_planned_hours += planned_hours
			person_work_hours += work_hours
			
			latex(u" & {hours:.0f} ({diff:+.0f})".format(
				hours = planned_hours,
				diff = work_hours - planned_hours
			), False)
		
		latex(u" & {hours:.0f} ({diff:+.0f})".format(
			hours = person_planned_hours,
			diff = person_work_hours - person_planned_hours
		), False)

		latex(u" \\\\")

	out.close()

def writeConsuntivoRole(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	planned_total_cost = 0
	planned_total_hours = 0
	worked_total_cost = 0
	worked_total_hours = 0
	for role in roles:
		role_costs = joinLists([
			[milestone.getPersonRoleCost(person, role) for person in project.getPeople()]
			for milestone in milestones
		])
		
		planned_cost = sum([c.getPlannedCost() for c in role_costs])
		planned_hours = sum([c.getPlannedHours() for c in role_costs])
		worked_cost = sum([c.getWorkHours() for c in role_costs])
		worked_hours = sum([c.getWorkCost() for c in role_costs])
		planned_total_cost += planned_cost
		planned_total_hours += planned_hours

		latex(u"\t{name} & {hours:.0f} ({diffH:+.0f}) & {cost:.0f} ({diffC:+.0f}) € \\\\".format(
			name = role.getName().title(),
			hours = planned_hours,
			cost = planned_cost,
			diffH = planned_hours - worked_hours,
			diffC = planned_cost - worked_cost
		))

	out.close()

def writeColumnChartOre(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))
		
	for role in roles:
		latex("\\addplot+[color={ruolo}] plotcoordinates".format(ruolo=role.getName().title()), False)
		latex("{",False)
		for person in sortByName(project.getPeople()):
			person_planned_hours = 0
			planned_hours = sum([m.getPersonRoleCost(person, role).getPlannedHours() for m in milestones])
			latex(u"({persona},{ore})".format(
				persona = person.getName(),
				ore = planned_hours
			), False)
		latex(u"};", True)

	out.close()

def writePieChartOreMilestone(project, milestone_id, roles_id, filename):
	milestone = project.getMilestone(str(milestone_id))
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))

	#planned_total_cost = 0
	planned_total_hours = 0
	latex(u"\\pie[text=legend, color={amministratore, analista, progettista, programmatore, responsabile, verificatore}]{", False)
	for role in roles:
		role_costs = [milestone.getPersonRoleCost(person, role) for person in project.getPeople()]
		planned_hours = sum([c.getPlannedHours() for c in role_costs])
		planned_total_hours += planned_hours

	firstentry = True
	for role in roles:
		role_costs = [milestone.getPersonRoleCost(person, role) for person in project.getPeople()]
		planned_hours = sum([c.getPlannedHours() for c in role_costs])

		if not firstentry:
			latex(u", ", False)
		firstentry = False

		if planned_hours != 0:
			latex(u"{ore:.1f}/{ruolo}".format(
				ruolo = role.getName().title(),
				ore = (planned_hours * 100 / planned_total_hours)
			), False)
		else:
			latex(u"./{ruolo}".format(
				ruolo = role.getName().title()
			), False)

	latex(u"}")
	
	out.close()

def writePieChartCosto(project, milestone_ids, roles_id, filename):
	milestones = [project.getMilestone(str(x)) for x in milestone_ids]
	roles = [project.getRole(str(role_id)) for role_id in roles_id]
	
	out = open(filename, "w")
	def latex(str, newline=True):
		out.write(str.encode('utf-8'))
		if newline:
			out.write("\n".encode('utf-8'))
	
	planned_total_cost = 0
	for role in roles:
		role_costs = joinLists([
			[milestone.getPersonRoleCost(person, role) for person in project.getPeople()]
			for milestone in milestones
		])
		planned_cost = sum([c.getPlannedCost() for c in role_costs])
		planned_total_cost += planned_cost
	
	firstentry = True
	latex(u"\\pie[text=legend, color={amministratore, analista, progettista, programmatore, responsabile, verificatore}]{", False)	
	for role in roles:
		planned_cost = 0
		role_costs = joinLists([[milestone.getPersonRoleCost(person, role) for person in project.getPeople()]for milestone in milestones
		])
		planned_cost = sum([c.getPlannedCost() for c in role_costs])
		if not firstentry:
			latex(u", ", False)
		firstentry = False
		
		if planned_cost != 0:
			latex(u"{costo:.1f}/{ruolo}".format(
				ruolo = role.getName().title(),
				costo = (planned_cost * 100 / planned_total_cost)
			), False)
		else:
			latex(u"./{ruolo}".format(
				ruolo = role.getName().title()
			), False)

	latex(u"}")

	out.close()

