migrate-db:
	alembic revision --autogenerate 
	alembic upgrade head