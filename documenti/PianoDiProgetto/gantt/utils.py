#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from parametri import *

def warning(message):
	print "ATTENZIONE: "+message.encode('utf-8')

def pedantic_warning(message):
	if not VERBOSE: return
	print "ATTENZIONE: "+message.encode('utf-8')

def printTitle(title):
	print
	print title
	print "".join(["-"]*len(title))
