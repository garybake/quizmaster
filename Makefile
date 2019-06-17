venv:
	python3.6 -m venv venv
	@echo 'export FLASK_APP=quiz.py' >> venv/bin/activate
	@echo 'export FLASK_DEBUG=1' >> venv/bin/activate

install_pips:
	pip install -r requirements.txt

create_db:
	python create_db.py

serve:
	flask run

build_report:
	go build -o docker/report ./report/src/report.go
	cd docker; docker build -t garybake/quiz .

run_report:
	docker run --network="host" garybake/quiz
