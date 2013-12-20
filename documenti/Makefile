 # Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all: test documents

documents:
	@cd "NormeDiProgetto" && make documents
	@cd "PianoDiProgetto" && make documents
	@cd "PianoDiQualifica" && make documents
	@cd "Glossario" && make documents
	@cd "LetteraDiPresentazione" && make documents
	@cd "Verbale2013-12-05" && make documents
	@cd "AnalisiDeiRequisiti" && make documents
	@cd "StudioDiFattibilita" && make documents
	@cd "Verbale2013-12-18" && make documents

test:
	@cd "NormeDiProgetto" && make test
	@cd "PianoDiProgetto" && make test
	@cd "PianoDiQualifica" && make test
	@cd "Glossario" && make test
	@cd "LetteraDiPresentazione" && make test
	@cd "Verbale2013-12-05" && make test
	@cd "AnalisiDeiRequisiti" && make test
	@cd "StudioDiFattibilita" && make test
	@cd "Verbale2013-12-18" && make test

clean:
	@rm -f *~
	@cd "NormeDiProgetto" && make clean
	@cd "PianoDiProgetto" && make clean
	@cd "PianoDiQualifica" && make clean
	@cd "Glossario" && make clean
	@cd "LetteraDiPresentazione" && make clean
	@cd "Verbale2013-12-05" && make clean
	@cd "AnalisiDeiRequisiti" && make clean
	@cd "StudioDiFattibilita" && make clean
	@cd "Verbale2013-12-18" && make clean

