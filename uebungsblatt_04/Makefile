TEST_CMD = python3 -m doctest
CHECKSTYLE_CMD = flake8

all: download unzip test checkstyle

no_download: test checkstyle

download:
	curl -o Downloads/AT.zip http://download.geonames.org/export/dump/AT.zip
	curl -o Downloads/allCountries.zip http://download.geonames.org/export/dump/allCountries.zip

unzip:
	unzip Downloads/AT.zip -d Textfiles
	unzip Downloads/allCountries.zip -d Textfiles

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
	rm Downloads/*
	rm Textfiles/*