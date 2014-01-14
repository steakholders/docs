 # Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

all:
	@make test-spelling
	@make documents

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
	@cd "SpecificaTecnica" && make documents

test-spelling:
	@cd "NormeDiProgetto" && make test-spelling
	@cd "PianoDiProgetto" && make test-spelling
	@cd "PianoDiQualifica" && make test-spelling
	@cd "Glossario" && make test-spelling
	@cd "LetteraDiPresentazione" && make test-spelling
	@cd "Verbale2013-12-05" && make test-spelling
	@cd "AnalisiDeiRequisiti" && make test-spelling
	@cd "StudioDiFattibilita" && make test-spelling
	@cd "Verbale2013-12-18" && make test-spelling
	@cd "SpecificaTecnica" && make test-spelling

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
	@cd "SpecificaTecnica" && make clean
