#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from parametri import *
from datetime import date

def warning(message):
	print "ATTENZIONE: "+message.encode('utf-8')

def pedantic_warning(message):
	if not VERBOSE: return
	print "ATTENZIONE: "+message.encode('utf-8')

def printTitle(title):
	print
	print title
	print "".join(["-"]*len(title))

def writeOnFile(filename, content):
	file_in = open(filename, "w")
	file_in.write(content)
	file_in.close()

def sortByStart(array):
	return sorted(array, key = lambda x: x.getStart() if x.getStart() is not None else date(year=1990,month=1,day=1))

def sortByName(array):
	return sorted(array, key = lambda x: x.name)