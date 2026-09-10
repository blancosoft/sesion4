@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\pythonw.exe" (
	echo No se encontro el entorno virtual .venv.
	echo Ejecute primero la instalacion indicada en README.md.
	pause
	exit /b 1
)

start "Sistema Experto Automatico" ".venv\Scripts\pythonw.exe" main.py
