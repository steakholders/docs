#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from schema import TaskList, Milestone, Task, TimeEntry
from datetime import date

def aggiungi(project, milestone_id):
	# id giusti
	giacomo = "62753"	
	enrico = "62754"	
	serena = "62755"	
	federico = "62756"	
	nicolo = "62757"
	luca = "62758"	
	gianluca = "62760"	

	inizio_fittizio = date(2010, 1, 1)
	fine_fittizia = date(2010, 1, 10)
	
	milestone = Milestone(project, str(milestone_id), fine_fittizia, "Analisi dei requisiti")
	project.addMilestone(milestone)
	
	tasklist = TaskList(milestone, 1, "AR", "TaskList Fittizia")
	milestone.addTaskList(tasklist)
		
	tabella = []
	tabella.append((federico, "analista", 9, 11))
	tabella.append((federico, "responsabile", 4, 3))
	tabella.append((federico, "verificatore", 9, 5))
	tabella.append((enrico, "analista", 12, 14))
	tabella.append((enrico, "progettista", 9, 10))
	tabella.append((enrico, "verificatore", 2, 2))
	tabella.append((giacomo, "amministratore", 9, 9))
	tabella.append((giacomo, "analista", 2, 2))
	tabella.append((giacomo, "responsabile", 5, 5))
	tabella.append((giacomo, "verificatore", 4, 4))
	tabella.append((gianluca, "analista", 10, 12))
	tabella.append((gianluca, "verificatore", 11, 6))
	tabella.append((luca, "amministratore", 6, 6))
	tabella.append((luca, "analista", 11, 13))
	tabella.append((nicolo, "amministratore", 15, 15))
	tabella.append((nicolo, "responsabile", 5, 5))
	tabella.append((serena, "analista", 14, 14))
	tabella.append((serena, "verificatore", 5, 5))
	
	for (id, (person, role, hours, time)) in enumerate(tabella):
		tasklist.addTask(Task(
			# 99999999+id per non far collidere gli id giusti con questi inventati
			tasklist, 99999999+id, inizio_fittizio, fine_fittizia, "AR", "Task fittizio "+str(id),
			responsible = project.getPerson(person),
			role = project.getRole(role),
			planned_hours = hours
		))
		tasklist.getTask(99999999+id).addTimeEntry(TimeEntry(99999999+id, 5555+id, time))
	
