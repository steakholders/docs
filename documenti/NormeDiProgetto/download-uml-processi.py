#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mechanize
import urllib
import re

def login (br, username, password):
	print "Eseguo il login per %s..." % username
	text = br.open("https://www.lucidchart.com/users/login").read()
	
	br.select_form(nr=0)
	br["username"] = username
	br["password"] = password
	
	print "Invio i dati per il login..."
	br.submit().read()

def download_image(br, userid, documentid, destination):
	"""
	Usa le api per le immagini:
	https://www.lucidchart.com/documents/image/<documentId>/<pageNum>/<width>/<square>
	DocumentId 	id of the document for which an image will be returned
	PageNum 	the page of the document for which an image will be returned
	width 	the width of the image to be returned
	square 	if 1 then return square image, otherwise return an image in the original aspect ratio
	"""
	
	print "Apro il documento %s..." % documentid
	doc = br.open("https://www.lucidchart.com/documents/view/%s" % documentid).read()
	pdfdata = ""
	for line in doc.split('\n'):
		if "pdfdata" in line:
			pdfdata = line
			break
	
	print pdfdata
	
	pdfdata = re.sub('^.*"pdfdata":', '', pdfdata)
	pdfdata = re.sub(',"Change":\[\].*$', '', pdfdata)
	
	print pdfdata
	
	return
	
	parameters = {
		'parameter1' : 'your content',
		'parameter2' : 'a constant value',
		'parameter3' : 'unique characters you might need to extract from the page'
	}
	#Encode the parameters
	data = urllib.urlencode(parameters)

	print "Genero l'immagine del documento %s..." % documentid
	result = br.open("https://www.lucidchart.com/documents/pdf/%s/%s/png/300" % (documentid, userid), data).read()
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
download_image(br, "101012627", "471f-1654-52ae2a57-ad48-71840a005f9d", "uml-processi/img.png")

