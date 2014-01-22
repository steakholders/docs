#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Includi la cartella /script/ nella path di ricerca degli import
import os, sys, inspect
currrentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.join(currrentdir, '../../script'))

from lucidchart import LucidchartClient

########################################
#  Istruzioni per la prima esecuzione  #
########################################

# 1- scaricare il programma Ngrok http://ngrok.com/
# 2- sul terminale A eseguire `ngrok 8888` (8888 è il valore della variabile server_port)
# 3- copiare l'indirizzo http://xyzxyz.ngrok.com
# 4- sul terminale B eseguire questo script con l'indirizzo http://xyzxyz.ngrok.com come primo parametro
#    cioè `python download_uml.py http://xyzxyz.ngrok.com`
# 5- aprire il link che lo script dirà di aprire
# 6- autorizzare lo script ad accedere a Lucidchart (cliccando su "permetti" nella pagina aperta con il link di prima)
# 7- dovrebbe aprirsi una pagina con scritto "tutto a posto" o qualcosa del genere, chiuderla pure
# 8- lo script dovrebbe scaricare tutto in automatico
# 9- chiudere pure Ngrok
# 10- la prossima volta non servirà Ngrok, basterà eseguire `python download_uml.py`

server_port = 8888

if len(sys.argv) <= 1:
	print "Alla prima esecuzione bisogna passare come primo argomento l'indirizzo a cui è raggiungibile la porta {server_port} di questo computer".format(server_port=server_port)
	callback_url = None
else:
	callback_url = sys.argv[1]


lucidchart = LucidchartClient(callback_url = callback_url, server_port=server_port)

lucidchart.download_image("4a67-2b94-52d5646f-a414-6aaa0a009db8", "uml/three_tier.png")
lucidchart.download_image("4e5d-5500-52dfaeac-975e-420b0a009998", "uml/architettura-generale-package.png")
