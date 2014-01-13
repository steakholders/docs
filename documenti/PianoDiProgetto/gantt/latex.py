#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def writeGanttLatex(project, milestone_id, filename):
	milestone = project.getMilestone(str(milestone_id))
	out = file.open(filename, "w")
	def latex(str):
		out.write(str+"\n")

	latex("\\begin\{ganttchart\}\{{start}\}\{{end}\}".format(start=milestone.getStart(), end=milestone.getEnd()))

	latex("\\end\{ganttchart\}")

	out.close()