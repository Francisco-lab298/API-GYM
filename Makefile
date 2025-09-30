start:
	python src/server.py

dev:
	watchmedo auto-restart --pattern="*.py" --recursive -- python src/server.py
