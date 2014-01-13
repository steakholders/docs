#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def warning(message):
	print "ATTENZIONE: "+message.encode('utf-8')

def pedantic_warning(message):
	disable = True
	if disable: return
	print "ATTENZIONE: "+message.encode('utf-8')

def printTitle(title):
	print
	print title
	print "".join(["-"]*len(title))
