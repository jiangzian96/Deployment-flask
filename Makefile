install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C model.py &&\
		pylint --disable=R,C app.py &&\
			pylint --disable=R,C request.py

train:
	python model.py