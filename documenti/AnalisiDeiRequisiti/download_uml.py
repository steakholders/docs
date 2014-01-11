#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Includi la cartella /script/ nella path di ricerca degli import
import os, sys, inspect
currrentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.join(currrentdir, '../../script'))

from lucidchart import LucidchartClient

##########
#  Main  #
##########

server_port = 8088

if len(sys.argv) <= 1:
	print "Alla prima esecuzione bisogna passare come primo argomento l'indirizzo a cui è raggiungibile la porta {server_port} di questo computer".format(server_port=server_port)
	callback_url = None
else:
	callback_url = sys.argv[1]


lucidchart = LucidchartClient(callback_url = callback_url, server_port=server_port)

# Download come png
# Se non è specificato come parametro
# - la larghezza è 600px
# - la pagina di cui scaricare il png è la 1
# es. lucidchart.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "UML/bla bla bla bla.png", width=600, pagenum=1)
lucidchart.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "UML/bla bla bla bla.png")
