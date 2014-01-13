#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

class TeamworkPMClient:
	def __init__(self, company="steakholders", key=None):
		self.company = company
		self.private_key_file = path.expanduser("~/.teamworkpm_private_key")
		self.key = ""
		
		# Ottieni la chiave privata
		if key is None or len(key) == 0:
			try:
				in_file = open(self.private_key_file, "r")
				self.key = json.load(in_file)
				in_file.close()
			except IOError:
				pass
		else:
			self.key = key
		
		# Chiedila se è vuota
		while self.key is None or len(self.key) == 0:
			self.key = raw_input(u"Inserisci la chiave privata per le API di TeamworkPM del tuo utente: ")	

		# Salva la chiave privata nella home (in chiaro!)
		out_file = open(self.private_key_file, "w")
		json.dump(self.key, out_file)
		out_file.close()

	def request(self, action):
		request = urllib2.Request("https://{0}.teamworkpm.net/{1}".format(self.company, action))
		request.add_header("Authorization", "BASIC " + base64.b64encode(self.key + ":xxx"))
		response = urllib2.urlopen(request)
		data = response.read()
		return data

	def requestJSON(self, base_action, parameters=""):
		action = base_action+".json"
		if len(parameters) > 0:
			action += "?" + parameters

		json_data = self.request(action)
		data = json.loads(json_data)
		return data
