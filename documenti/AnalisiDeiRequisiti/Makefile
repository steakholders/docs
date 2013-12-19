# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ../..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk


all: test documents

documents: download $(CURR_DIR_NAME).pdf

# Compila il file LaTeX principale
$(CURR_DIR_NAME).pdf: *.tex $(MODEL_FILES)
	@$(REPO_DIR)/script/compile-latex.sh

# Con questo trucchetto viene creato un file vuoto, la cui data di modifica
# viene usata dal makefile per decidere se è necessario rieseguire i comandi.
test: test.cache
test.cache: *.tex $(DICTIONARIES)
	@$(REPO_DIR)/script/test-encoding.sh
	@$(REPO_DIR)/script/test-spelling.sh
	@touch test.cache

clean:
	@rm -f test.cache
	@rm -f *.log *.tex.backup
	@rm -f *~
	@rm -f *.aux *.out *.toc
	@rm -f *.pdf
	@rm -f *.tex.bak

download: 
	@./download_requisiti.py
