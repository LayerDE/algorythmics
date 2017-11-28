TEST_CMD = python3 -m doctest
C_COMPILER = gcc -shared -fPIC -Os -std=c99 
CHECKSTYLE_CMD = flake8

all: test checkstyle

compile:
	$(C_COMPILER) *.c -ldl -o *.so

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
