#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from Queue import PriorityQueue
from collections import namedtuple

from gantt_lib import Factory, warning, pedantic_warning, error

MIN_HOURS = 95
MAX_HOURS = 105
MAX_HOURS_PER_DAY = 3
MIN_ESTIMATE_COST = 13000
MAX_ESTIMATE_COST = 13999
MIN_VERIFIER_PERCENT = 0.3

def printTitle(title):
	print
	print title
	print "".join(["-"]*len(title))

def printProjectReport(project):
	printTitle("Riepilogo progetto")

	print "Milestone: {num}".format(num=len(project.milestones))
	print "Persone: {num}".format(num=len(project.people))
	print "Ruoli: {num}".format(num=len(project.roles))
	print "TaskList: {num}".format(num=len(project.tasklists))
	print "Task: {num}".format(num=len(project.tasks))

def printTaskLists(project):
	printTitle("Elenco delle tasklist")

	for l in project.tasklists.values():
		print "* {nome} da {start} a {end}: {num} task".format(
			nome = l.name,
			start = l.getStart(),
			end = l.getEnd(),
			num = len(l.tasks)
		)

def testTasks(project):
	printTitle("Controllo vincoli sui task")
	
	for task in project.getTasks():
		# Avvisa se ci sono più di MAX_HOURS_PER_DAY ore per giorno
		if task.hours > (task.end - task.start).days * MAX_HOURS_PER_DAY:
			warning(u'Al task "{name}" sono state assegnate troppe ore ({hours}, {max_hours})'.format(
				name = self.name,
				hours = self.hours,
				max_hours = (self.end - self.start).days * MAX_HOURS_PER_DAY
			))

def testPerson(project):
	printTitle("Controllo vincoli sulle persone")
	
	# Visualizza informazioni
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		hours = sum([t.hours for t in tasks])
		print u"- {nome}: \t{hours} \tore di lavoro".format(nome=person.name, hours=hours).encode("utf-8")

	print

	# Controlla vincoli sulle ore di lavoro
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		hours = sum([t.hours for t in tasks])
		
		if hours < MIN_HOURS:
			warning(u"{name} ({hours} h) deve fare almeno {min} ore di lavoro".format(
				hours=hours,
				name=person.name,
				min=MIN_HOURS
			))

		if hours > MAX_HOURS:
			warning(u"{name} ({hours} h) deve fare almassimo {max} ore di lavoro".format(
				hours=hours,
				name=person.name,
				max=MAX_HOURS
			))

def testConcurrentTask(project):
	printTitle("Controllo che tutti abbiano da fare un solo task alla volta")
	
	# Controlla che tutti abbiano da fare un solo task alla volta
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		
		Range = namedtuple('Range', ['date', 'edge'])
		queue = PriorityQueue()
		start = 0
		end = 1

		for task in tasks:
			queue.put(Range(date=task.start, edge=start))
			queue.put(Range(date=task.end, edge=end))

		open_task = 0
		while not queue.empty():
			(date, edge) = queue.get()
			current_date = date

			# Esamina tutti i task di questo giorno
			while date == current_date:
				if edge == start:
					open_task += 1
				if edge == end:
					open_task -= 1
				date = None

				if not queue.empty():
					(date, edge) = queue.get()
			
			if date is not None:
				queue.put(Range(date=date, edge=edge))

			# Controlla se ci sono troppi task aperti
			if open_task < 0 or open_task > 1:
				warning("{nome} ha più di un task ({num}) segnato per il giorno {date}".format(
					nome = person.name,
					num = open_task,
					date = current_date
				))
				break

def estimateCosts(project):
	printTitle("Controllo vincoli sul preventivo")
	role_cost = []
	role_hours = []
	verifier_hours = None

	for role in project.getRoles():
		tasks = [t for t in project.getTasks() if t.role == role]
		hours = sum([t.hours for t in tasks])
		cost = hours * role.hour_cost
		
		role_cost.append(cost)
		role_hours.append(hours)
		if role.name == "verificatore":
			verifier_hours = hours

		print u"- {nome}: {hours} \tore, per un costo di \t{costo} \t€".format(
			nome=role.name +"".join([" "]*(14-len(role.name))),
			hours=hours,
			costo=cost
		).encode("utf-8")

	total_cost = sum(role_cost)
	total_hours = sum(role_hours)
	print u"Totale          : {total} €".format(total=total_cost).encode("utf-8")
	print u"Ore di verifica : {perc:.1f} %".format(perc=100*verifier_hours/total_hours).encode("utf-8")

	print
	
	if verifier_hours < total_hours * MIN_VERIFIER_PERCENT:
		warning(u"Troppe poche ore di verifica ({verifier_hours} h), bisogna fare almeno {min_verifier_hours} h".format(
			verifier_hours = verifier_hours,
			min_verifier_hours =  total_hours * MIN_VERIFIER_PERCENT
		))
	

	if total_cost < MIN_ESTIMATE_COST:
		warning(u"Il preventivo ({total} €) è troppo basso, bisogna raggiungere almeno {min} €".format(
			total=total_cost,
			min=MIN_ESTIMATE_COST
		))

	if total_cost > MAX_ESTIMATE_COST:
		warning(u"Il preventivo ({total} €) è meglio che sia inferiore a {max} €".format(
			total=total_cost,
			max=MAX_ESTIMATE_COST
		))

project = Factory.createProject("steakholders", id=65465)
project.load()

printProjectReport(project)
printTaskLists(project)

testTasks(project)
testPerson(project)
testConcurrentTask(project)

estimateCosts(project)