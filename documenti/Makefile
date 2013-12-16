# Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all: test documents

documents:
	@cd "NormeDiProgetto" && make documents
	@cd "PianoDiProgetto" && make documents

test:
	@cd "NormeDiProgetto" && make test
	@cd "PianoDiProgetto" && make test

clean:
	@rm -f *~
	@cd "NormeDiProgetto" && make clean
	@cd "PianoDiProgetto" && make clean

