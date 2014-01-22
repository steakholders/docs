#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from schema import TaskList, Milestone, Task

def aggiungi(project, milestone_id):
	# id giusti
	federico = 62756	
	serena = 62757	
	luca = 62758	
	gianluca = 62760	
	enrico = 62754	
	nicolo = 62757	
	giacomo = 62753	
	
	milestone = Milestone(project, milestone_id, None, "Analisi dei requisiti")
	project.addMilestone(milestone)
	
	tasklist = TaskList(milestone, 1, "AR", "Fittizia")
	milestone.addTaskList(tasklist)
		
	tabella = []
	tabella.append((federico, "analisi", 9))
	tabella.append((federico, "responsabile", 4))
	tabella.append((federico, "verificatore", 9))
	tabella.append((enrico, "analista", 12))
	tabella.append((enrico, "progettista", 9))
	tabella.append((enrico, "verificatore", 2))
	tabella.append((giacomo, "amministratore", 9))
	tabella.append((giacomo, "analista", 2))
	tabella.append((giacomo, "responsabile", 5))
	tabella.append((giacomo, "verificatore", 4))
	tabella.append((gianluca, "analista", 10))
	tabella.append((gianluca, "verificatore", 11))
	tabella.append((luca, "amministratore", 6))
	tabella.append((luca, "analista", 11))
	tabella.append((nicolo, "amministratore", 15))
	tabella.append((nicolo, "responsabile", 5))
	tabella.append((serena, "analista", 14))
	tabella.append((serena, "verificatore", 5))
	
	for (id, (person, role, hours)) in enumerate(tabella):
		tasklist.addTask(Task(
			# 999999 per non far collidere gli id giusti con questi inventati
			tasklist, 99999999+id, None, None, "AR", "Name "+str(id),
			responsible = project.getPerson(person),
			role = project.getRole(role),
			planned_hours = hours
		))
	
