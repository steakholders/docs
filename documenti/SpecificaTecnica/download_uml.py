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

#uml Scenari 

lucidchart.download_image("40ef-da14-52e92878-b851-4bb70a009cc4", "scenari/requireNotLogged ERROR.png")
lucidchart.download_image("4f11-86bc-52ea65a0-aff2-549c0a004801", "scenari/requireLogged ERROR.png")
lucidchart.download_image("43f3-86c8-52ea65e3-854b-0c250a00c886", "scenari/requireAdmin ERROR.png")
lucidchart.download_image("45cd-59b4-52ea2c2c-9040-6b370a008a7d", "scenari/Profile GET.png")
lucidchart.download_image("4580-25b0-52ea2df5-affc-20e90a005d4c", "scenari/Password Lost POST.png")
lucidchart.download_image("49f9-a62c-52e92143-8edb-76fb0a005953", "scenari/logout DELETE.png")
lucidchart.download_image("4388-2c2c-52ea2ed0-9f92-3dcb0a008a7d", "scenari/Password Reset PUT.png")
lucidchart.download_image("4b4b-d5b4-52ea2d23-b9d5-3fd60a00c886", "scenari/Profile PUT.png")
lucidchart.download_image("474b-5340-52ea2f14-821c-54130a0080fd", "scenari/Users GET.png")
lucidchart.download_image("4cd0-6af8-52ea4779-a369-46c60a008a7d", "scenari/Action Name Collection Document PUT.png")
lucidchart.download_image("4a49-1fc8-52ea472b-9701-30250a00c886", "scenari/Action Name Collection PUT.png")
lucidchart.download_image("43d0-05a0-52ea4645-8262-14280a008a7d", "scenari/Collection Name Document POST.png")
lucidchart.download_image("4435-7f0c-52ea451d-99a0-35980a008a7d", "scenari/Collection Name GET.png")
lucidchart.download_image("492e-8840-52ea42b6-a97b-53570a00ca2b", "scenari/Users Id DELETE.png")
lucidchart.download_image("4686-92d4-52ea3266-b7ee-6a310a005d4c", "scenari/Users Id POST.png")
lucidchart.download_image("4dd8-efd4-52e91e57-bc0a-0f790a00c47f", "scenari/login POST.png")
lucidchart.download_image("4924-b25c-52ea46e4-98d0-041b0a00c886", "scenari/Collection Name Document DELETE.png")
lucidchart.download_image("4dfc-0ffc-52ea43b0-adbc-2ae30a00c47f", "scenari/Collection GET.png")
lucidchart.download_image("4b55-e628-52ea3161-84f4-1cfe0a008a7d", "scenari/Users Id GET.png")
lucidchart.download_image("4caa-b984-52ea3079-80dc-54820a0080fd", "scenari/Users POST.png")
lucidchart.download_image("4fb7-7948-52ea45c2-a882-6f990a00c886", "scenari/Collection Name Document GET.png")

lucidchart.download_image("4b48-aacc-52e916f6-8d9b-7f110a0080fd", "scenari/Diagramma Routing Richiesta.png")
lucidchart.download_image("426d-99f8-52e9169b-a010-263b0a0049fb", "scenari/Diagramma Gestione Richiesta.png")



