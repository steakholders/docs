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


lucidchart.download_image("4e5d-5500-52dfaeac-975e-420b0a009998", "uml/architettura-generale-package.png", width=1600)

lucidchart.download_image("481c-f134-52eadfb8-b89d-38f60a009f36", "uml/diagramma-classi-front-end.png", width=1600)

lucidchart.download_image("4d01-fab4-52dac262-8caf-6d3b0a0044cb", "uml/MaaP - Apri pagina gestione utenti.png")
lucidchart.download_image("43ed-3f84-52d93755-a6c3-500d0a004790", "uml/MaaP - Modifica profilo.png")

lucidchart.download_image("4bdc-1928-52dac052-9e58-4fc30a004790", "uml/MaaP - Modifica document.png")
lucidchart.download_image("4c35-b374-52d8f514-8852-77310a00c655", "uml/MaaP - Attività principali.png")
lucidchart.download_image("440c-f4bc-52dabbcb-a162-0c630a004790", "uml/MaaP - Show-page.png")
lucidchart.download_image("47b2-4774-52d98c99-872c-04f90a00d7c9", "uml/MaaP - Index-page.png")
lucidchart.download_image("4709-9388-52d930e7-9fdc-44290a009998", "uml/MaaP - Effettua login.png")
lucidchart.download_image("4cf6-0efc-52d93535-84d0-514a0a009db8", "uml/MaaP - Esegui reset password.png")
lucidchart.download_image("4023-a820-52d92c89-96e5-4fff0a00d7c9", "uml/MaaP - Recupera password.png")
lucidchart.download_image("4bba-c714-52d92c1c-8bb1-46e50a0044cb", "uml/MaaP - Effettua registrazione.png")
lucidchart.download_image("4580-bc10-52dac665-b8a4-5aa60a0044cb", "uml/MaaP - Apri show-page utente.png")
lucidchart.download_image("4611-1c34-52dac3ad-9b7e-22830a00d361", "uml/MaaP - Crea nuovo utente.png")


