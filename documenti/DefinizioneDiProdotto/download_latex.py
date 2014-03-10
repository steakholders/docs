#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Forse sarà necessario installare il pacchetto python-mechanize
# credevo che non avesse dipendenze, ricordavo male
import mechanize

class RequisteakClient:
	def __init__(self):
		self.browser = mechanize.Browser()

	def login(self, username="admin@steakholders.com", password=""):
		print "Eseguo il login..."
		text = self.browser.open("https://steakholders.herokuapp.com/users/sign_in")
		self.browser.select_form(nr = 0)
		self.browser["user[email]"] = username
		self.browser["user[password]"] = password
		text = self.browser.submit().read()
		
		if "Signed in successfully" not in text:
			print "Errore: login fallito"
			return False
		else:
			return True

	def download(self, link, destination):
		print "Scarico %s in %s" % (link, destination)
		text = self.browser.open(link).read();
		
		out_file = open(destination,"w")
		out_file.write(text)
		out_file.close()


##########
#  Main  #
##########

username = "admin@steakholders.com"
password = None

while password is None or len(password) == 0:
	password = raw_input("Password per {username}: ".format(username=username))

requisteak = RequisteakClient()
if requisteak.login(username, password):
	requisteak.download("http://steakholders.herokuapp.com/downloads/front-end-definition", "frontend-definition.tex")
	requisteak.download("http://steakholders.herokuapp.com/downloads/back-end-definition", "backend-definition.tex")
