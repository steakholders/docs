# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ../..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

# Includi il makefile di default dei documenti.
# Se servisse, sostituire questa inclusione con il codice specializzato.
include $(REPO_DIR)/script/default-doc.mk

download-gantt:
	@python download_gantt.py 2>&1 | tee esito_gantt.txt