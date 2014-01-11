# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all: test-spelling

# Con questo trucchetto viene creato un file vuoto, la cui data di modifica
# viene usata dal makefile per decidere se è necessario rieseguire i comandi.
test-spelling: test-spelling.cache
test-spelling.cache: *.tex $(DICTIONARIES)
	@$(REPO_DIR)/script/test-encoding.sh
	@$(REPO_DIR)/script/test-spelling.sh
	@touch test.cache

clean:
	@rm -f *.cache
	@rm -f *.log *.tex.backup
	@rm -f *~
