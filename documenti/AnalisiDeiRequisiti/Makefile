# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ../..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

# Includi il makefile di default dei documenti.
# Se servisse, sostituire questa inclusione con il codice specializzato.
include $(REPO_DIR)/script/default-doc.mk

download-requisiti:
	@python download_requisiti.py

download-uml:
	@python download_uml.py
