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

lucidchart.download_image("471f-1654-52ae2a57-ad48-71840a005f9d", "uml-processi/richiesta_di_modifica_e_segnalazione_bug.png")
lucidchart.download_image("4c30-fde4-52d337d8-8fc7-71b80a005548", "uml-processi/progettazione_unita_di_lavoro.png")
lucidchart.download_image("4aa8-02e4-52ae2830-9412-5cb50a0086f4", "uml-processi/valutazione_issue.png")
lucidchart.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "uml-processi/pianificazione_issue.png")
lucidchart.download_image("4901-7cc4-52ae1b50-a03c-42480a0086f4", "uml-processi/creazione_task.png")
lucidchart.download_image("4557-ff54-52ae279d-8ccc-58080a00c462", "uml-processi/esecuzione_verifica.png")
lucidchart.download_image("45ee-6c9c-52ae271d-88b0-07070a0086f4", "uml-processi/esecuzione_compito.png")
