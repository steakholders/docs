# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all: test documents

documents:
	@cd "PianoDiQualifica" && make documents

test:
	@cd "PianoDiQualifica" && make test

clean:
	@rm -f *~
	@cd "PianoDiQualifica" && make clean

