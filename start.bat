@echo off
echo Iniciando o servidor Flask...
set FLASK_APP=src/routes/app-rotas.py
set FLASK_ENV=development
flask run
