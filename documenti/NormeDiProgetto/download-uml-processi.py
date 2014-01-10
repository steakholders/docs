#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import BaseHTTPServer
from urlparse import urlparse, parse_qs
from rauth import OAuth1Service
from os import path
import thread
import time
import sys
import json

# globale
server_port = 8080
verifier = None

class AuthHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		global verifier
		params = parse_qs(urlparse(self.path).query)
		if 'oauth_verifier' in params:
			verifier = params['oauth_verifier'][0]
			self.log_message("Ottenuto il verifier {verifier} ({url})".format(verifier=verifier, url=self.path))
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write("<html><body><h1>Perfetto!</h1><h4>Ora torna pure al tuo script</h4></body></html>")

def runAuthServer(port):
	httpd = BaseHTTPServer.HTTPServer(("", port), AuthHandler)
	httpd.serve_forever()

class LucidchartClient:
	def __init__(self, session_file="~/.lucidchart", callback_url=""):
		"""
		session_file: il file in cui memorizzare i token di accesso
		callback_url: l'indirizzo a cui è raggiungibile il server in ascolto sulla porta {server_port} di questo computer
		"""
		# Get a real consumer key & secret from https://dev.lucidchart.com/apps/new
		self.lucidchart = OAuth1Service(
			name='lucidchart',
			consumer_key='19fc0b404e04768b61cf4eff52688a0975cab033',
			consumer_secret='22fed08f0d0b6e4f64a435ffa3ef6a8e5337924b',
			request_token_url='https://www.lucidchart.com/oauth/requestToken',
			access_token_url='https://www.lucidchart.com/oauth/accessToken',
			authorize_url='https://www.lucidchart.com/oauth/authorize',
			base_url='https://www.lucidchart.com/'
		)
		self.session_file = path.expanduser(session_file)
		self.callback_url = callback_url
	
	def new_session(self):
		global verifier
		
		print "Faccio partire il server"
		thread.start_new_thread(runAuthServer,(server_port,))
		time.sleep(1)
		
		if not self.callback_url:
			print "Server una url di callback valida, della forma 'http://example.com/"
			return None
		
		data = {'oauth_callback': self.callback_url}
		request_token, request_token_secret = self.lucidchart.get_request_token(data=data)
		authorize_url = self.lucidchart.get_authorize_url(request_token)
		
		print "Visita questa url nel tuo browser: {url}".format(url=authorize_url)
		print "Attendo che venga inviata l'autorizzazione a {callback}...".format(callback=self.callback_url)
		while verifier == None:
			time.sleep(1)
		print "Autorizzazione ricevuta"
	
		session = self.lucidchart.get_auth_session(
			request_token,
			request_token_secret,
			method='POST',
			data = {'oauth_verifier': verifier}
		)
		
		out_file = open(self.session_file, "w")
		json.dump((session.access_token, session.access_token_secret), out_file)
		out_file.close()
		
		return session
	
	def reuse_session(self):
		try:
			in_file = open(self.session_file, "r")
			access_token, access_token_secret = json.load(in_file)
			in_file.close()
		except IOError as e:
			return None
		
		session = self.lucidchart.get_session((access_token, access_token_secret))
		return session

	def init_session(self):
		session = self.reuse_session()
		if not session:
			session = self.new_session()
		return session
	
	def download_image(self, document, destination):
		"""
		document: l'id del documento di lucidchart
		destination: la posizione in cui salvare le immagini
		"""
		session = self.init_session()
		
		print "Scarico il documento {docid} in {destination} ...".format(docid=document, destination=destination)
		r = session.get('https://www.lucidchart.com/documents/image/{docid}/{pagenum}/{width}/{square}'.format(docid=document, pagenum=1, width=600, square=0), verify=True)
		
		out_file = open(destination,"w")
		out_file.write(r.content)
		out_file.close()


if len(sys.argv) <= 1:
	print "Alla prima esecuzione bisogna passare come primo argomento l'indirizzo a cui è raggiungibile la porta {server_port} di questo computer".format(server_port=server_port)
	callback_url = None
else:
	callback_url = sys.argv[1]

lc = LucidchartClient(callback_url = callback_url)


lc.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "uml-processi/Pianificazione_compito_e_verifica.png")
lc.download_image("471f-1654-52ae2a57-ad48-71840a005f9d", "uml-processi/Richiesta_di_modifica_e_segnalazione_bug.png")
lc.download_image("4aa8-02e4-52ae2830-9412-5cb50a0086f4", "uml-processi/Valutazione_delle_modifiche.png")
lc.download_image("4557-ff54-52ae279d-8ccc-58080a00c462", "uml-processi/Esecuzione_verifica.png")
lc.download_image("45ee-6c9c-52ae271d-88b0-07070a0086f4", "uml-processi/Esecuzione_compito.png")
lc.download_image("4901-7cc4-52ae1b50-a03c-42480a0086f4", "uml-processi/Creazione_compito.png")

