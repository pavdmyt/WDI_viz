flake:
	flake8 viz.py 
	
clean:
	rm -f `find . -type f -name '*.py[co]'`

