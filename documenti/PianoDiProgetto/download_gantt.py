#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from gantt.schema import *
from gantt.download import *
from gantt.process import *
from gantt.latex import *
from gantt.dati_rr import *

tw = TeamworkPMDownload("steakholders")
project = Project(id=65465)

print "Scarico Milestones..."
tw.getMilestones(project)
print "Scarico People..."
tw.getPeople(project)
print "Scarico TaskLists..."
tw.getTaskLists(project)
print "Scarico TimeEntries..."
tw.getTimeEntries(project)
print "Scaricamento completato."

milestone_rr = 999999 # tenere 999999
milestone_rp = 103264
milestone_rq = 103265
milestone_ra = 104204

testTasks(project)
testTaskLists(project)
testConcurrentTasks(project)
testEstimateCosts(project, [milestone_rp, milestone_rq, milestone_ra])
testPeople(project)

aggiungi(project, milestone_rr)

writeGanttMilestone(project, milestone_rp, "gantt_rp.tex")
writeGanttMilestone(project, milestone_rq, "gantt_rq.tex")
writeGanttMilestone(project, milestone_ra, "gantt_ra.tex")

writeRipartizioneOre(project, [milestone_rp], "ripartizione_rp.tex")
writeRipartizioneOre(project, [milestone_rq], "ripartizione_rq.tex")
writeRipartizioneOre(project, [milestone_ra], "ripartizione_ra.tex")

roles = [
	"amministratore",
	"analista",
	"progettista",
	"programmatore",
	"responsabile",
	"verificatore"
]

writeSuddivisioneOre(project, [milestone_rr], roles, "suddivisione_rr.tex")
writeSuddivisioneOre(project, [milestone_rp], roles, "suddivisione_rp.tex")
writeSuddivisioneOre(project, [milestone_rq], roles, "suddivisione_rq.tex")
writeSuddivisioneOre(project, [milestone_ra], roles, "suddivisione_ra.tex")
writeSuddivisioneOre(project, [milestone_rp, milestone_rq, milestone_ra], roles, "suddivisione_totale.tex")
writeSuddivisioneOre(project, [milestone_rr, milestone_rp, milestone_rq, milestone_ra], roles, "suddivisione_totale_con_analisi.tex")

writeColumnChartOre(project, [milestone_rr], roles, "columnChart_rr.tex")
writeColumnChartOre(project, [milestone_rp], roles, "columnChart_rp.tex")
writeColumnChartOre(project, [milestone_rq], roles, "columnChart_rq.tex")
writeColumnChartOre(project, [milestone_ra], roles, "columnChart_ra.tex")
writeColumnChartOre(project, [milestone_rp, milestone_rq, milestone_ra], roles, "columnChart_totale.tex")
writeColumnChartOre(project, [milestone_rr, milestone_rp, milestone_rq, milestone_ra], roles, "columnChart_totale_con_analisi.tex")

writePieChartCosto(project, [milestone_rr], roles, "pieChart_costo_rr.tex")
writePieChartCosto(project, [milestone_rp], roles, "pieChart_costo_rp.tex")
writePieChartCosto(project, [milestone_rq], roles, "pieChart_costo_rq.tex")
writePieChartCosto(project, [milestone_ra], roles, "pieChart_costo_ra.tex")
writePieChartCosto(project, [milestone_rp, milestone_rq, milestone_ra], roles, "pieChart_costo_totale.tex")

writePieChartOreMilestone(project, milestone_rr, roles, "pieChart_rr.tex")
writePieChartOreMilestone(project, milestone_rp, roles, "pieChart_rp.tex")
writePieChartOreMilestone(project, milestone_rq, roles, "pieChart_rq.tex")
writePieChartOreMilestone(project, milestone_ra, roles, "pieChart_ra.tex")

writeProspetto(project, [milestone_rr], roles, "prospetto_rr.tex")
writeProspetto(project, [milestone_rp], roles, "prospetto_rp.tex")
writeProspetto(project, [milestone_rq], roles, "prospetto_rq.tex")
writeProspetto(project, [milestone_ra], roles, "prospetto_ra.tex")
writeProspetto(project, [milestone_rp, milestone_rq, milestone_ra], roles, "prospetto_totale.tex")


writeConsuntivoRole(project, [milestone_rr], roles, "consuntivo_roles_rr.tex")
writeConsuntivoRole(project, [milestone_rp], roles, "consuntivo_roles_rp.tex")

writeColumnChartConsuntivo(project, [milestone_rr], roles, "columnChart_consuntivo_rr.tex")
writeColumnChartConsuntivo(project, [milestone_rp], roles, "columnChart_consuntivo_rp.tex")

writeConsuntivoComponent(project, [milestone_rr], roles, "consuntivo_component_rr.tex")
writeConsuntivoComponent(project, [milestone_rp], roles, "consuntivo_component_rp.tex")

# Consuntivo totale
writeConsuntivoComponent(project, [milestone_rr, milestone_rp], roles, "consuntivo_component_totale.tex")
writeConsuntivoRole(project, [milestone_rr, milestone_rp], roles, "consuntivo_roles_totale.tex")
