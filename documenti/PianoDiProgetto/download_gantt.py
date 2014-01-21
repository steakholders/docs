#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from gantt.schema import *
from gantt.download import *
from gantt.process import *
from gantt.latex import *

tw = TeamworkPMDownload("steakholders")
project = Project(id=65465)

print "Scarico Milestones..."
tw.getMilestones(project)
print "Scarico People..."
tw.getPeople(project)
print "Scarico TaskLists..."
tw.getTaskLists(project)
#print "Scarico TimeEntries..."
#tw.getTimeEntries(project)
print "Scaricamento completato."


testTasks(project)
testPeople(project)
testConcurrentTasks(project)

milestone_rr = 101586
milestone_rp = 103264
milestone_rq = 103265
milestone_ra = 104204

testEstimateCosts(project, [milestone_rp, milestone_rq, milestone_ra])

writeGanttMilestone(project, milestone_rp, "gantt_rp.tex")
writeGanttMilestone(project, milestone_rq, "gantt_rq.tex")
writeGanttMilestone(project, milestone_ra, "gantt_ra.tex")

writeRipartizioneOreMilestone(project, milestone_rp, "ripartizione_rp.tex")
writeRipartizioneOreMilestone(project, milestone_rq, "ripartizione_rq.tex")
writeRipartizioneOreMilestone(project, milestone_ra, "ripartizione_ra.tex")

roles = [
	"amministratore",
	"analista",
	"progettista",
	"programmatore",
	"responsabile",
	"verificatore"
]

writeSuddivisioneOreMilestone(project, milestone_rp, roles, "suddivisione_rp.tex")
writeSuddivisioneOreMilestone(project, milestone_rq, roles, "suddivisione_rq.tex")
writeSuddivisioneOreMilestone(project, milestone_ra, roles, "suddivisione_ra.tex")
writeSuddivisioneOreTotale(project, [milestone_rp, milestone_rq, milestone_ra], roles, "suddivisione_totale.tex")

writeColumnChartOreMilestone(project, milestone_rp, roles, "columnChart_rp.tex")
writeColumnChartOreMilestone(project, milestone_rq, roles, "columnChart_rq.tex")
writeColumnChartOreMilestone(project, milestone_ra, roles, "columnChart_ra.tex")
# writeColumnChartOreTotale(project, [milestone_rp, milestone_rq, milestone_ra], roles, "columnChart_totale.tex")

writePieChartOreMilestone(project, milestone_rp, roles, "pieChart_rp.tex")
writePieChartOreMilestone(project, milestone_rq, roles, "pieChart_rq.tex")
writePieChartOreMilestone(project, milestone_ra, roles, "pieChart_ra.tex")
# writePieChartOreTotale(project, [milestone_rp, milestone_rq, milestone_ra], roles, "pieChart_totale.tex")

writeProspettoMilestone(project, milestone_rp, roles, "prospetto_rp.tex")
writeProspettoMilestone(project, milestone_rq, roles, "prospetto_rq.tex")
writeProspettoMilestone(project, milestone_ra, roles, "prospetto_ra.tex")
writeProspettoTotale(project, [milestone_rp, milestone_rq, milestone_ra], roles, "prospetto_totale.tex")

writeConsuntivoTotale(project, [milestone_rp, milestone_rq, milestone_ra], roles, "consuntivo_totale.tex")
