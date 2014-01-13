#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
from gantt.schema import *
from gantt.download import *
from gantt.process import *
from gantt.latex import *

tw = TeamworkPMDownload("steakholders")
project = Project(id=65465)

tw.getMilestones(project)
tw.getPeople(project)
tw.getTaskLists(project)
tw.getTimeEntries(project)


testTasks(project)
testPeople(project)
testConcurrentTasks(project)

milestone_rr = 101586
milestone_rp = 103264
milestone_rq = 103265
milestone_ra = 104204

testEstimateCosts(project, [milestone_rp, milestone_rq, milestone_ra])

writeGanttLatex(project, milestone_rr, "gantt_rr.tex")
