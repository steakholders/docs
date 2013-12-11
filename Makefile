# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = .

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all: test documents

documents:
	@cd "documenti" && make documents

test:
	@cd "documenti" && make test

test-glossary:
	@$(REPO_DIR)/script/test-glossary.sh

test-regexp:
	@$(REPO_DIR)/script/test-regex.sh

clean:
	@rm -f *~
	@cd "documenti" && make clean
	@cd "modello" && make clean
	@cd "script" && make clean

