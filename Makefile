# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = .

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all:
	@make test-spelling
	@make documents

documents:
	+cd "documenti" && make documents

test-spelling:
	@cd "documenti" && make test-spelling
	@cd "modello" && make test-spelling

test-glossary:
	@$(REPO_DIR)/script/test-glossary.sh

test-regexp:
	@$(REPO_DIR)/script/test-regex.sh

gulpease:
	@$(REPO_DIR)/script/pdftotxt.sh

clean:
	@rm -f *~
	@cd "documenti" && make clean
	@cd "modello" && make clean
	@cd "script" && make clean

build: test documents
	@mkdir -p "build"
	@rm -f build/*.pdf build/documenti-pdf.zip
	@for file in documenti/*/*.pdf; do echo "[*] Copio $$file in build/"; cp "$$file" "build/"; done
	@cd build && zip documenti-pdf.zip *.pdf
	@echo "[*] L'archivio build/documenti-pdf.zip è pronto"

