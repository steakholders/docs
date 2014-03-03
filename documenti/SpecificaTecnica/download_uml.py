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

lucidchart.download_image("437d-f4e4-52efd47d-907f-3aaf0a00c7a5", "uml/deployment.png", width=1600)

# diagrammi di attività

lucidchart.download_image("4d01-fab4-52dac262-8caf-6d3b0a0044cb", "uml/attività/MaaP - Apri pagina gestione utenti.png")
lucidchart.download_image("43ed-3f84-52d93755-a6c3-500d0a004790", "uml/attività/MaaP - Modifica profilo.png")
lucidchart.download_image("4bdc-1928-52dac052-9e58-4fc30a004790", "uml/attività/MaaP - Modifica document.png")
lucidchart.download_image("4c35-b374-52d8f514-8852-77310a00c655", "uml/attività/MaaP - Attivita principali.png")
lucidchart.download_image("440c-f4bc-52dabbcb-a162-0c630a004790", "uml/attività/MaaP - Show-page.png")
lucidchart.download_image("47b2-4774-52d98c99-872c-04f90a00d7c9", "uml/attività/MaaP - Index-page.png")
lucidchart.download_image("4709-9388-52d930e7-9fdc-44290a009998", "uml/attività/MaaP - Effettua login.png")
lucidchart.download_image("4cf6-0efc-52d93535-84d0-514a0a009db8", "uml/attività/MaaP - Esegui reset password.png")
lucidchart.download_image("4023-a820-52d92c89-96e5-4fff0a00d7c9", "uml/attività/MaaP - Recupera password.png")
lucidchart.download_image("4bba-c714-52d92c1c-8bb1-46e50a0044cb", "uml/attività/MaaP - Effettua registrazione.png")
lucidchart.download_image("4580-bc10-52dac665-b8a4-5aa60a0044cb", "uml/attività/MaaP - Apri show-page utente.png")
lucidchart.download_image("4611-1c34-52dac3ad-9b7e-22830a00d361", "uml/attività/MaaP - Crea nuovo utente.png")
lucidchart.download_image("4262-6030-52ebb3ee-8efa-06e70a0048dc", "uml/attività/MaaS - Attivita principali.png")
lucidchart.download_image("43a8-3e2c-52ed0031-8ac6-11420a0048dc", "uml/attività/MaaS - Gestisci file di configurazione.png")
lucidchart.download_image("4ff5-dafc-52ed0192-b270-1b550a00c7a5", "uml/attività/MaaS - Crea file di configurazione.png")
lucidchart.download_image("4dfb-2698-52ed0f8b-9e03-50580a0048dc", "uml/attività/Framework - Diagramma di installazione.png")
lucidchart.download_image("44d6-9194-52ee820c-8332-30020a0048dc", "uml/attività/Framework - Crea cartella front-end di default.png")

# uml Scenari

lucidchart.download_image("40ef-da14-52e92878-b851-4bb70a009cc4", "uml/scenari/requireNotLogged ERROR.png")
lucidchart.download_image("4f11-86bc-52ea65a0-aff2-549c0a004801", "uml/scenari/requireLogged ERROR.png")
lucidchart.download_image("43f3-86c8-52ea65e3-854b-0c250a00c886", "uml/scenari/requireAdmin ERROR.png")
lucidchart.download_image("45cd-59b4-52ea2c2c-9040-6b370a008a7d", "uml/scenari/Profile GET.png")
lucidchart.download_image("4580-25b0-52ea2df5-affc-20e90a005d4c", "uml/scenari/Password Forgot POST.png")
lucidchart.download_image("49f9-a62c-52e92143-8edb-76fb0a005953", "uml/scenari/logout DELETE.png")
lucidchart.download_image("4b4b-d5b4-52ea2d23-b9d5-3fd60a00c886", "uml/scenari/Profile PUT.png")
lucidchart.download_image("474b-5340-52ea2f14-821c-54130a0080fd", "uml/scenari/Users GET.png")
lucidchart.download_image("4cd0-6af8-52ea4779-a369-46c60a008a7d", "uml/scenari/Action Name Collection Document PUT.png")
lucidchart.download_image("4a49-1fc8-52ea472b-9701-30250a00c886", "uml/scenari/Action Name Collection PUT.png")
lucidchart.download_image("43d0-05a0-52ea4645-8262-14280a008a7d", "uml/scenari/Collection Name Document PUT.png")
lucidchart.download_image("4435-7f0c-52ea451d-99a0-35980a008a7d", "uml/scenari/Collection Name GET.png")
lucidchart.download_image("492e-8840-52ea42b6-a97b-53570a00ca2b", "uml/scenari/Users Id DELETE.png")
lucidchart.download_image("4686-92d4-52ea3266-b7ee-6a310a005d4c", "uml/scenari/Users Id PUT.png")
lucidchart.download_image("4dd8-efd4-52e91e57-bc0a-0f790a00c47f", "uml/scenari/login POST.png")
lucidchart.download_image("4924-b25c-52ea46e4-98d0-041b0a00c886", "uml/scenari/Collection Name Document DELETE.png")
lucidchart.download_image("4dfc-0ffc-52ea43b0-adbc-2ae30a00c47f", "uml/scenari/Collection GET.png")
lucidchart.download_image("4b55-e628-52ea3161-84f4-1cfe0a008a7d", "uml/scenari/Users Id GET.png")
lucidchart.download_image("4caa-b984-52ea3079-80dc-54820a0080fd", "uml/scenari/Users POST.png")
lucidchart.download_image("4fb7-7948-52ea45c2-a882-6f990a00c886", "uml/scenari/Collection Name Document GET.png")

lucidchart.download_image("4b48-aacc-52e916f6-8d9b-7f110a0080fd", "uml/scenari/Diagramma Routing Richiesta.png")
lucidchart.download_image("426d-99f8-52e9169b-a010-263b0a0049fb", "uml/scenari/Diagramma Gestione Richiesta.png")

# Back-end, Front-end e packages

lucidchart.download_image("42ee-aa18-52ee214e-97c2-1b760a00c7a5", "uml/classi/Back-end")
lucidchart.download_image("481c-f134-52eadfb8-b89d-38f60a009f36", "uml/classi/Front-end.png")

lucidchart.download_image("4503-9b84-52ed294c-bcab-649a0a00d8ac", "uml/package/Back-end.png")
lucidchart.download_image("4b82-f668-52ee5c3c-a084-129e0a004eaf", "uml/package/Back-end::DeveloperProject.png")
lucidchart.download_image("417e-3274-52efb757-8482-2fec0a004eaf", "uml/package/Back-end::Lib.png")
lucidchart.download_image("45fd-9d18-530efd72-8ab9-34430a005bed", "uml/package/Back-end::Lib::Model.png")
lucidchart.download_image("4e24-fb68-52ee5c82-baf3-79d10a009f36", "uml/package/Back-end::Lib::View.png")
lucidchart.download_image("46a9-31e4-52ee5e28-b3cb-3a540a004eaf", "uml/package/Back-end::Lib::Controller.png")
lucidchart.download_image("4764-99d8-52ee6346-816b-3e850a009f36", "uml/package/Back-end::Lib::Model::DSLModel.png")
lucidchart.download_image("4e50-af68-5308deea-8459-466f0a005bed", "uml/package/Back-end::Lib::Controller::Middleware.png")
lucidchart.download_image("46a9-31e4-52ee5e28-b3cb-3a540a004eaf", "uml/package/Back-end::Lib::Controller::Controller.png")

lucidchart.download_image("46db-fe50-52ee59b2-9159-104d0a00d8ac", "uml/package/Front-end.png")
lucidchart.download_image("4222-7be4-52ee445b-8b0c-34fa0a00d8ac", "uml/package/Front-end::Controllers.png")
lucidchart.download_image("4a09-4850-52ee4370-a63f-1ccd0a008772", "uml/package/Front-end::Services.png")
lucidchart.download_image("48ba-c3f8-52efbb7d-b3ee-3d760a008cac", "uml/package/Front-end::Model.png")


# Design pattern - contestualizzazione

lucidchart.download_image("460b-0034-52ee5d18-8e58-1b740a00c7a5", "patterns/contestualizzazione/middleware.png");
lucidchart.download_image("45f7-3c94-5308e7a5-a7b0-72850a005bed", "patterns/contestualizzazione/registry.png");
lucidchart.download_image("4ca7-e2d0-5308ee50-931b-56930a00cc50", "patterns/contestualizzazione/factory-method.png");
lucidchart.download_image("4395-1dac-530a11f7-9fe0-0fde0a005bed", "patterns/contestualizzazione/chain-of-responsability.png");
lucidchart.download_image("4879-d7d0-530a152d-8294-42aa0a0055ba", "patterns/contestualizzazione/strategy.png");
lucidchart.download_image("42e5-7fac-530a178b-9ed7-56be0a00cc50", "patterns/contestualizzazione/command.png");
