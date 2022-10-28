service_up:
	sudo docker compose up -d 

service_down:
	sudo docker compose down

connect_db:
	psql postgresql://postgres:password@0.0.0.0:5433/database

drawing:
	pipenv run python -c 'import lottery; lottery.drawing()'

init_db:
	pipenv run python -c 'import lottery; lottery.init_db()'