#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gantt_lib import Factory

project = Factory.createProject("steakholders", 65465)
project.load()

print "Milestone: {num}".format(num=len(project.milestones))
print "Persone: {num}".format(num=len(project.people))
print "Ruoli: {num}".format(num=len(project.roles))
print "TaskList: {num}".format(num=len(project.tasklists))
print "Task aperti: {num}".format(num=len(project.tasks))
