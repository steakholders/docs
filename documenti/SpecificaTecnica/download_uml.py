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

###########################################################
#  Istruzioni per cambiare la risoluzione delle immagini  #
###########################################################

# 1 - Dalla root della repository aprire script/lucidchart.py;
# 2 - Alla definizione del metodo download_image modificare il parametro "width";
# 3 - Se non si specifica niente prende un valore di default.

server_port = 8888

if len(sys.argv) <= 1:
	print "Alla prima esecuzione bisogna passare come primo argomento l'indirizzo a cui è raggiungibile la porta {server_port} di questo computer".format(server_port=server_port)
	callback_url = None
else:
	callback_url = sys.argv[1]


lucidchart = LucidchartClient(callback_url = callback_url, server_port=server_port)

lucidchart.download_image("437df4e4-52ef-d47d-907f-3aaf0a00c7a5", "uml/deployment.png", width=1600)

# diagrammi di attività

lucidchart.download_image("4d01fab4-52da-c262-8caf-6d3b0a0044cb", "uml/attivita/MaaP - Apri pagina gestione utenti.png")
lucidchart.download_image("43ed3f84-52d9-3755-a6c3-500d0a004790", "uml/attivita/MaaP - Modifica profilo.png")
lucidchart.download_image("4bdc1928-52da-c052-9e58-4fc30a004790", "uml/attivita/MaaP - Modifica document.png")
lucidchart.download_image("4c35b374-52d8-f514-8852-77310a00c655", "uml/attivita/MaaP - Attivita principali.png")
lucidchart.download_image("440cf4bc-52da-bbcb-a162-0c630a004790", "uml/attivita/MaaP - Show-page.png")
lucidchart.download_image("47b24774-52d9-8c99-872c-04f90a00d7c9", "uml/attivita/MaaP - Index-page.png")
lucidchart.download_image("47099388-52d9-30e7-9fdc-44290a009998", "uml/attivita/MaaP - Effettua login.png")
lucidchart.download_image("4cf60efc-52d9-3535-84d0-514a0a009db8", "uml/attivita/MaaP - Esegui reset password.png")
lucidchart.download_image("4023a820-52d9-2c89-96e5-4fff0a00d7c9", "uml/attivita/MaaP - Recupera password.png")
lucidchart.download_image("4bbac714-52d9-2c1c-8bb1-46e50a0044cb", "uml/attivita/MaaP - Effettua registrazione.png")
lucidchart.download_image("4580bc10-52da-c665-b8a4-5aa60a0044cb", "uml/attivita/MaaP - Apri show-page utente.png")
lucidchart.download_image("46111c34-52da-c3ad-9b7e-22830a00d361", "uml/attivita/MaaP - Crea nuovo utente.png")
lucidchart.download_image("42626030-52eb-b3ee-8efa-06e70a0048dc", "uml/attivita/MaaS - Attivita principali.png")
lucidchart.download_image("43a83e2c-52ed-0031-8ac6-11420a0048dc", "uml/attivita/MaaS - Gestisci file di configurazione.png")
lucidchart.download_image("4ff5dafc-52ed-0192-b270-1b550a00c7a5", "uml/attivita/MaaS - Crea file di configurazione.png")
lucidchart.download_image("4dfb2698-52ed-0f8b-9e03-50580a0048dc", "uml/attivita/Framework - Diagramma di installazione.png")
lucidchart.download_image("44d69194-52ee-820c-8332-30020a0048dc", "uml/attivita/Framework - Crea cartella front-end di default.png")

# uml Scenari

lucidchart.download_image("40efda14-52e9-2878-b851-4bb70a009cc4", "uml/scenari/requireNotLogged ERROR.png")
lucidchart.download_image("4f1186bc-52ea-65a0-aff2-549c0a004801", "uml/scenari/requireLogged ERROR.png")
lucidchart.download_image("43f386c8-52ea-65e3-854b-0c250a00c886", "uml/scenari/requireAdmin ERROR.png")
lucidchart.download_image("4b188a48-5319-9709-9815-27c00a00d013", "uml/scenari/requireSuperAdmin ERROR.png")
lucidchart.download_image("45cd59b4-52ea-2c2c-9040-6b370a008a7d", "uml/scenari/Profile GET.png")
lucidchart.download_image("458025b0-52ea-2df5-affc-20e90a005d4c", "uml/scenari/Password Forgot POST.png")
lucidchart.download_image("49f9a62c-52e9-2143-8edb-76fb0a005953", "uml/scenari/profile DELETE.png")
lucidchart.download_image("4b4bd5b4-52ea-2d23-b9d5-3fd60a00c886", "uml/scenari/Profile PUT.png")
lucidchart.download_image("474b5340-52ea-2f14-821c-54130a0080fd", "uml/scenari/Users GET.png")
lucidchart.download_image("4cd06af8-52ea-4779-a369-46c60a008a7d", "uml/scenari/Action Name Collection Document PUT.png")
lucidchart.download_image("4a491fc8-52ea-472b-9701-30250a00c886", "uml/scenari/Action Name Collection PUT.png")
lucidchart.download_image("43d005a0-52ea-4645-8262-14280a008a7d", "uml/scenari/Collection Name Document PUT.png")
lucidchart.download_image("44357f0c-52ea-451d-99a0-35980a008a7d", "uml/scenari/Collection Name GET.png")
lucidchart.download_image("492e8840-52ea-42b6-a97b-53570a00ca2b", "uml/scenari/Users Id DELETE.png")
lucidchart.download_image("468692d4-52ea-3266-b7ee-6a310a005d4c", "uml/scenari/Users Id PUT.png")
lucidchart.download_image("4dd8efd4-52e9-1e57-bc0a-0f790a00c47f", "uml/scenari/profile POST.png")
lucidchart.download_image("4924b25c-52ea-46e4-98d0-041b0a00c886", "uml/scenari/Collection Name Document DELETE.png")
lucidchart.download_image("4dfc0ffc-52ea-43b0-adbc-2ae30a00c47f", "uml/scenari/Collection GET.png")
lucidchart.download_image("4b55e628-52ea-3161-84f4-1cfe0a008a7d", "uml/scenari/Users Id GET.png")
lucidchart.download_image("4caab984-52ea-3079-80dc-54820a0080fd", "uml/scenari/Users POST.png")
lucidchart.download_image("4fb77948-52ea-45c2-a882-6f990a00c886", "uml/scenari/Collection Name Document GET.png")

lucidchart.download_image("4b48aacc-52e9-16f6-8d9b-7f110a0080fd", "uml/scenari/Diagramma Routing Richiesta.png")
lucidchart.download_image("426d99f8-52e9-169b-a010-263b0a0049fb", "uml/scenari/Diagramma Gestione Richiesta.png")

# Back-end, Front-end e packages

lucidchart.download_image("42eeaa18-52ee-214e-97c2-1b760a00c7a5", "uml/classi/Back-end.png")
lucidchart.download_image("481cf134-52ea-dfb8-b89d-38f60a009f36", "uml/classi/Front-end.png")

lucidchart.download_image("45039b84-52ed-294c-bcab-649a0a00d8ac", "uml/package/Back-end.png")
lucidchart.download_image("4b82f668-52ee-5c3c-a084-129e0a004eaf", "uml/package/Back-end::DeveloperProject.png")
lucidchart.download_image("417e3274-52ef-b757-8482-2fec0a004eaf", "uml/package/Back-end::Lib.png")
lucidchart.download_image("424f5ba4-5314-928a-be35-38d40a00d329", "uml/package/Back-end::Lib::Utils.png")
lucidchart.download_image("45fd9d18-530e-fd72-8ab9-34430a005bed", "uml/package/Back-end::Lib::Model.png")
lucidchart.download_image("4e24fb68-52ee-5c82-baf3-79d10a009f36", "uml/package/Back-end::Lib::View.png")
lucidchart.download_image("42962830-530e-fb46-9960-23df0a009107", "uml/package/Back-end::Lib::Controller.png")
lucidchart.download_image("476499d8-52ee-6346-816b-3e850a009f36", "uml/package/Back-end::Lib::Model::DSLModel.png")
lucidchart.download_image("4e50af68-5308-deea-8459-466f0a005bed", "uml/package/Back-end::Lib::Controller::Middleware.png")
lucidchart.download_image("46a931e4-52ee-5e28-b3cb-3a540a004eaf", "uml/package/Back-end::Lib::Controller::Service.png")

lucidchart.download_image("46dbfe50-52ee-59b2-9159-104d0a00d8ac", "uml/package/Front-end.png")
lucidchart.download_image("42227be4-52ee-445b-8b0c-34fa0a00d8ac", "uml/package/Front-end::Controllers.png")
lucidchart.download_image("4a094850-52ee-4370-a63f-1ccd0a008772", "uml/package/Front-end::Services.png")
lucidchart.download_image("48bac3f8-52ef-bb7d-b3ee-3d760a008cac", "uml/package/Front-end::Model.png")
lucidchart.download_image("4145e0c0-5320-6524-8aba-3b3e0a005c63", "uml/package/Front-end::View.png")

# Design pattern - contestualizzazione

lucidchart.download_image("460b0034-52ee-5d18-8e58-1b740a00c7a5", "patterns/contestualizzazione/middleware.png");
lucidchart.download_image("45f73c94-5308-e7a5-a7b0-72850a005bed", "patterns/contestualizzazione/registry.png");
lucidchart.download_image("4ca7e2d0-5308-ee50-931b-56930a00cc50", "patterns/contestualizzazione/factory-method.png");
lucidchart.download_image("43951dac-530a-11f7-9fe0-0fde0a005bed", "patterns/contestualizzazione/chain-of-responsability.png");
lucidchart.download_image("4879d7d0-530a-152d-8294-42aa0a0055ba", "patterns/contestualizzazione/strategy.png");
lucidchart.download_image("42e57fac-530a-178b-9ed7-56be0a00cc50", "patterns/contestualizzazione/command.png");
