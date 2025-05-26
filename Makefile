
install:
	pip install -r requirements.txt

run:
	jupyter notebook

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type d -name '.ipynb_checkpoints' -exec rm -r {} +

freeze:
	pip freeze > requirements.txt
