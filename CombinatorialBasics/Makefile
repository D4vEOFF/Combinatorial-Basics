TEXCOMPILER = pdflatex
BIBCOMPILER = bibtex

.PHONY: all compile clean compile-no-bibtex

all: compile clean

all-no-bibtex: compile-no-bibtex clean

compile: combinatorics.tex
	${TEXCOMPILER} combinatorics.tex
	${BIBCOMPILER} combinatorics
	${TEXCOMPILER} combinatorics.tex
	${TEXCOMPILER} combinatorics.tex

compile-no-bibtex:
	${TEXCOMPILER} combinatorics.tex
	${TEXCOMPILER} combinatorics.tex

clean:
	# del *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi *.synctex.gz /f /s
	rm -Rf *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi *.synctex.gz