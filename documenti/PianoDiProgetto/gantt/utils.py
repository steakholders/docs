#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import date
import re
from parametri import *

class GanttException(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return "ERRORE: "+self.message.encode('utf-8')

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

def joinLists(array):
	joined = []
	for x in array:
		joined.extend(x)
	return joined

def sortByName(array):
	return sorted(array, key = lambda x: x.getName())

def sortByStart(array):
	return sorted(array, key = lambda x: x.getStart() if x.getStart() is not None else date(year=1990,month=1,day=1))

def sortByCode(array):
	def weight(code):
		nome = re.sub('[^a-zA-Z]', '', code)
		gerarchia = re.sub('[a-zA-Z]', '', code)
		
		peso_nome = 0
		if nome == "AN":  peso_nome = 10
		if nome == "PA":  peso_nome = 20
		if nome == "PDC": peso_nome = 30
		if nome == "VV":  peso_nome = 40
		if nome == "V":  peso_nome = 45

		return [peso_nome]+[int(x) for x in gerarchia.split('.')]

	return sorted(array, key = lambda x: weight(x.getCode()))
