#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from Queue import PriorityQueue
from collections import namedtuple
from datetime import timedelta

from gantt_lib import Factory, warning, pedantic_warning

# Numero minimo e massimo di ore di lavoro a testa
MIN_HOURS = 95
MAX_HOURS = 105
# Minimo e massimo di ore di lavoro al giorno per mersona
MIN_HOURS_PER_DAY = 1
MAX_HOURS_PER_DAY = 3
# Numero minimo di ruoli che una persona deve svolgere, ciascuno per almeno tot ore
MIN_ROLES_PER_PERSON = 6
MIN_HOURS_PER_PERSON_ROLE = 2
# Percentuale massima di ore che una persona può passare su un unico ruolo
MAX_PERCENT_ON_ROLE_PER_PERSON = 0.5
# Preventivo minimo e massimo, percentuale minima di ore di verifica
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
		if task.hours > task.getDays() * MAX_HOURS_PER_DAY:
			warning(u'Al task "{name}" sono state assegnate troppe ore (sono {hours}, al massimo {max_hours})'.format(
				name = task.name,
				hours = task.hours,
				max_hours = task.getDays() * MAX_HOURS_PER_DAY
			))

		# Avvisa se ci sono meno di MIN_HOURS_PER_DAY ore per giorno
		if task.hours < task.getDays() * MIN_HOURS_PER_DAY:
			warning(u'Al task "{name}" sono state assegnate troppe poche ore (sono {hours}, al minimo {min_hours})'.format(
				name = task.name,
				hours = task.hours,
				min_hours = task.getDays() * MIN_HOURS_PER_DAY
			))

def testPerson(project):
	printTitle("Controllo vincoli sulle persone")
	
	# Visualizza informazioni
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		hours = sum([t.hours for t in tasks])
		print u"- {nome}: \t{hours:.0f} \tore di lavoro".format(nome=person.name, hours=hours).encode("utf-8")

	print
	
	# Visualizza informazioni
	for person in project.getPeople():
		personal_tasks = [t for t in project.getTasks() if t.responsible == person]
		total_hours = sum([t.hours for t in personal_tasks])
		personal_roles = []

		for role in project.getRoles():
			tasks = [t for t in personal_tasks if t.role == role]
			hours = sum([t.hours for t in tasks])
			personal_roles.append((hours, role))

			if hours > total_hours * MAX_PERCENT_ON_ROLE_PER_PERSON:
				warning(u"{name} ({total:.0f} h) ha troppe ore come {role} ({hours:.0f} h), siamo a {perc:.0f}% (max {max:.0f}%)".format(
					name=person.name,
					total=total_hours,
					role=role.name,
					hours=hours,
					perc=100*hours/total_hours,
					max=100*MAX_PERCENT_ON_ROLE_PER_PERSON
				))

		current_roles = [r[1] for r in personal_roles if r[0] >= MIN_HOURS_PER_PERSON_ROLE]

		if len(current_roles) < MIN_ROLES_PER_PERSON:
			warning(u"{name} ha troppi pochi ruoli ({num}). Dovrebbe fare più {roles}.".format(
				name=person.name,
				num=len(current_roles),
				roles=", ".join([r.name for r in project.getRoles() if r not in current_roles])
			))

	print

	# Controlla vincoli sulle ore di lavoro
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		hours = sum([t.hours for t in tasks])
		
		if hours < MIN_HOURS:
			warning(u"{name} ({hours:.0f} h) deve fare almeno {min:.0f} ore di lavoro".format(
				hours=hours,
				name=person.name,
				min=MIN_HOURS
			))

		if hours > MAX_HOURS:
			warning(u"{name} ({hours:.0f} h) deve fare almassimo {max:.0f} ore di lavoro".format(
				hours=hours,
				name=person.name,
				max=MAX_HOURS
			))

def testConcurrentTask(project):
	printTitle("Controllo task sovrapposti")
	
	# Controlla che tutti abbiano da fare un solo task alla volta
	for person in project.getPeople():
		tasks = [t for t in project.getTasks() if t.responsible == person]
		
		Range = namedtuple('Range', ['date', 'edge'])
		queue = PriorityQueue()
		start = 0
		end = 1

		for task in tasks:
			queue.put(Range(date=task.start, edge=start))
			queue.put(Range(date=task.end+timedelta(days=1), edge=end))

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
				warning(u"{nome} ha dei task sovrapposti. Il primo è il giorno {date}".format(
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

		print u"- {nome}: {hours:.0f} \tore, per un costo di \t{costo:.0f} \t€".format(
			nome=role.name +"".join([" "]*(14-len(role.name))),
			hours=hours,
			costo=cost
		).encode("utf-8")

	total_cost = sum(role_cost)
	total_hours = sum(role_hours)
	print u"Totale          : {total:.0f} €".format(total=total_cost).encode("utf-8")
	print u"Ore di verifica : {perc:.1f} %".format(perc=100*verifier_hours/total_hours).encode("utf-8")

	print
	
	if verifier_hours < total_hours * MIN_VERIFIER_PERCENT:
		warning(u"Troppe poche ore di verifica ({verifier_hours:.0f} h), bisogna fare almeno {min_verifier_hours:.0f} h".format(
			verifier_hours = verifier_hours,
			min_verifier_hours =  total_hours * MIN_VERIFIER_PERCENT
		))
	

	if total_cost < MIN_ESTIMATE_COST:
		warning(u"Il preventivo ({total:.0f} €) è troppo basso, bisogna raggiungere almeno {min:.0f} €".format(
			total=total_cost,
			min=MIN_ESTIMATE_COST
		))

	if total_cost > MAX_ESTIMATE_COST:
		warning(u"Il preventivo ({total:.0f} €) è meglio che sia inferiore a {max:.0f} €".format(
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
