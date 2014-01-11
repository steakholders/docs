#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Includi la cartella /script/ nella path di ricerca degli import
import os, sys, inspect
currrentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, os.path.join(currrentdir, '../../script'))

from lucidchart import LucidchartClient


server_port = 8088

if len(sys.argv) <= 1:
	print "Alla prima esecuzione bisogna passare come primo argomento l'indirizzo a cui è raggiungibile la porta {server_port} di questo computer".format(server_port=server_port)
	callback_url = None
else:
	callback_url = sys.argv[1]


lc = LucidchartClient(callback_url = callback_url, server_port=server_port)

lc.download_image("4f51-1824-52ae25da-a646-74fd0a00d457", "uml-processi/Pianificazione_compito_e_verifica.png")
lc.download_image("471f-1654-52ae2a57-ad48-71840a005f9d", "uml-processi/Richiesta_di_modifica_e_segnalazione_bug.png")
lc.download_image("4aa8-02e4-52ae2830-9412-5cb50a0086f4", "uml-processi/Valutazione_delle_modifiche.png")
lc.download_image("4557-ff54-52ae279d-8ccc-58080a00c462", "uml-processi/Esecuzione_verifica.png")
lc.download_image("45ee-6c9c-52ae271d-88b0-07070a0086f4", "uml-processi/Esecuzione_compito.png")
lc.download_image("4901-7cc4-52ae1b50-a03c-42480a0086f4", "uml-processi/Creazione_compito.png")
