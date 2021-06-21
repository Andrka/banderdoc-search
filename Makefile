req:
	poetry export -f requirements.txt --output requirements.txt

isort:
	poetry run isort app

lint:
	poetry run flake8 app

run:
	poetry run uvicorn app.main:app --reload

image-build:
	docker build -t banderdoc-search .

image-run:
	docker run -d --name banderdoc-search -p 80:80 banderdoc-search