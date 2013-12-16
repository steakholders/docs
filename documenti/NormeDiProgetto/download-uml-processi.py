#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mechanize

def login (br, username, password):
	print "Eseguo il login per %s..." % username
	text = br.open("https://www.lucidchart.com/users/login").read()
	
	br.select_form(nr=0)
	br["username"] = username
	br["password"] = password
	
	print "Invio i dati per il login..."
	br.submit().read()

def download_image(br, documentid, destination):
	"""
	Usa le api per le immagini:
	https://www.lucidchart.com/documents/image/<documentId>/<pageNum>/<width>/<square>
	DocumentId 	id of the document for which an image will be returned
	PageNum 	the page of the document for which an image will be returned
	width 	the width of the image to be returned
	square 	if 1 then return square image, otherwise return an image in the original aspect ratio
	"""
	
	print "Genero l'immagine del documento %s..." % documentid
	result = br.open("https://www.lucidchart.com/documents/pdf/%s/101012627/png/300" % documentid).read()
	print result
	
	if '"success":false' in result:
		return False
	
	print "Scarico l'immagine del documento %s..." % documentid
	image = br.open("https://www.lucidchart.com/documents/download/%s" % documentid).read()
	#image = br.open("https://www.lucidchart.com/documents/image/%s/%s/%s/0" % (documentid, pagenum, width)).read()
	
	out_file = open(destination,"w")
	out_file.write(image)
	out_file.close()
	


br = mechanize.Browser()
username = "federico.poli.1@studenti.unipd.it"
password = raw_input('Inserisci la password per %s:' % username)
login(br, username, password)
download_image(br, "471f-1654-52ae2a57-ad48-71840a005f9d", "uml-processi/img.png")

