#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gantt_lib import Factory

project = Factory.createProject("steakholders", id=65465)
project.load()

print
print "Riepilogo progetto"
print "------------------"
print "Milestone totali: {num}".format(num=len(project.milestones))
print "Persone totali: {num}".format(num=len(project.people))
print "Ruoli totali: {num}".format(num=len(project.roles))
print "TaskList aperte: {num}".format(num=len(project.tasklists))
print "Task aperti: {num}".format(num=len(project.tasks))
