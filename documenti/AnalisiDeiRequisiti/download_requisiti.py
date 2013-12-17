#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Forse sarà necessario installare il pacchetto python-mechanize
# credevo che non avesse dipendenze, ricordavo male
import mechanize

def login (br):
	print "Eseguo il login..."
	text = br.open("https://steakholders.herokuapp.com/admin/login")
	br.select_form(nr = 0)
	br["admin_user[email]"] = "admin@steakholders.com"
	br["admin_user[password]"] = "steakazzi"
	text = br.submit().read()
	
	if "Signed in successfully" not in text:
		print "Errore: login fallito"
		

def download(br, link, destination):
	print "Scarico %s in %s" % (link, destination)
	text = br.open(link).read();
	
	out_file = open(destination,"w")
	out_file.write(text)
	out_file.close()

##########
#  Main  #
##########

br = mechanize.Browser()
login(br)
download(br, "https://steakholders.herokuapp.com/admin/export_use_cases", "capitolo-use-case.tex")
download(br, "https://steakholders.herokuapp.com/admin/export_requisites", "capitolo-requisiti.tex")

