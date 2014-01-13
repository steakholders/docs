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

# Download come png
# Se non è specificato come parametro, di default
# - la larghezza è 600px
# - la pagina di cui scaricare il png è la 1
# es. lucidchart.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "UML/bla bla bla bla.png", width=600, pagenum=1)

#UML AMBITO UTENTE
lucidchart.download_image("430a-6fb0-52a701a4-82e0-5eb50a00c811", "UML/UCU - Operazioni ad alto livello.png")
lucidchart.download_image("4c69-50c0-52a7197f-aa9b-1feb0a005f9d", "UML/UCU1 - Login.png")
lucidchart.download_image("443d-3480-52aad5a8-aba7-4eae0a0086f4", "UML/UCU5 - Registrazione.png")
lucidchart.download_image("4659-2270-52b21d23-bce8-196b0a00dea9", "UML/UCU7 - Gestione indici.png")
lucidchart.download_image("4d79-8410-52a72d62-8d0c-72aa0a00c462", "UML/UCU9 - Apertura Collection Index.png")
lucidchart.download_image("4265-792c-52a73039-a934-41f60a005f9d", "UML/UCU9.1 - Apertura show-page Document.png")
lucidchart.download_image("4c73-4560-52aaed73-83b3-40820a00d457", "UML/UCU10 - Modifica Profilo.png")
lucidchart.download_image("482c-b2e4-52a73b22-9361-34180a009f85", "UML/UCU11 - Gestione utenti.png")
lucidchart.download_image("4b7b-431c-52a73bc9-898c-552e0a00c811", "UML/UCU11.1 - Creazione Utente.png")
lucidchart.download_image("478e-3890-52b02514-9bb1-1a050a00c462", "UML/UCU11.3 - Apertura show-page Utente.png")

lucidchart.download_image("4c0e-8c78-52d3f94e-9c77-118c0a009902?", "UML/UCU4 - Recupero password.png")
lucidchart.download_image("4f18-b848-52d3fefb-a245-23890a00d44d?", "UML/UCU4.1 - Richiesta reset password.png")
lucidchart.download_image("4ad1-71f4-52d408a5-9481-3c2f0a00cb95?", "UML/UCU4.2 - Effettuazione reset password.png")
lucidchart.download_image("", "UML/.png")
lucidchart.download_image("", "UML/.png")
lucidchart.download_image("", "UML/.png")

#UML AMBITO SVILUPPATORE
lucidchart.download_image("47e2-6998-52a85f0a-a1b4-55cd0a00c462", "UML/UCS - Operazioni ad alto livello.png")
lucidchart.download_image("4ddd-fbf0-52a97bae-bbab-32110a009f85", "UML/UCS2 - Configurazione database.png")
lucidchart.download_image("4df6-7b64-52a86f52-b01c-16320a00c462", "UML/UCS3 - Gestione Collection.png")
lucidchart.download_image("4af3-92a4-52a882cb-bcad-1aef0a0086f4", "UML/UCS3.3 - Configurazione  Collection.png")
lucidchart.download_image("429b-795c-52a8840b-8a61-2e420a009f85", "UML/UCS3.3.1 - Personalizzazione index page.png")
lucidchart.download_image("41f9-8f68-52a88caa-9e42-09da0a00c462", "UML/UCS3.3.2 - Personalizzazione show page.png")
#UML AMBITO MAAS
lucidchart.download_image("49ed-78a8-52b1a3c1-8a77-3ddc0a00dea9", "UML/UCM - Operazioni ad alto livello.png")
lucidchart.download_image("43a0-e1c8-52b385b6-ab48-59f90a00dea9", "UML/UCM1 - Registrazione.png")
lucidchart.download_image("4ab7-1b8c-52b3864d-8eb7-4a7b0a009f85", "UML/UCM4 - Login.png")
lucidchart.download_image("4608-6404-52b38737-8513-792a0a005e00", "UML/UCM6 - Modifica profilo.png")
lucidchart.download_image("47d4-44e0-52b1a49b-9b0b-6cf60a0052b1", "UML/UCM8 - Gestione file di configurazione.png")
