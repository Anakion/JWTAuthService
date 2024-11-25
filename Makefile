generate-key:
	openssl rand -hex 32
	tree
	poetry run alembic init -t async alembic
	poetry run alembic revision --autogenerate -m "Initial migration"
	poetry run alembic upgrade head