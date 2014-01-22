 # Percorso relativo alla cartella principale del repository, senza slash finale.
REPO_DIR = ..

# Includi i comandi comuni a tutti i makefile.
include $(REPO_DIR)/script/global.mk

DOCUMENTS = \
	NormeDiProgetto \
	PianoDiProgetto \
	PianoDiQualifica \
	Glossario \
	LetteraDiPresentazione \
	Verbale2013-12-05 \
	AnalisiDeiRequisiti \
	StudioDiFattibilita \
	Verbale2013-12-18 \
	SpecificaTecnica

all:
	@make test-spelling
	@make documents

# Permette di lanciarli in parallelo con -j 8
documents: $(DOCUMENTS:=.doc)
%.doc:
	@cd "$(@:.doc=)" && make documents

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
