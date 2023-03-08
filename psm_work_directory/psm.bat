@echo off

:: The Python Virtual Environment Path (aka "python.exe" file)
SET PYTHON_VIRTUAL_ENVIRONMENT=%~dp0\venv\Scripts\python.exe

:: The PSM Entry Point Path (aka "psm_main.py" file)
SET PSM_ENTRY_POINT=%~dp0\py_scripts\main_psm.py

:: This line calls the main_psm.py python file using the defined python environment
%PYTHON_VIRTUAL_ENVIRONMENT% %PSM_ENTRY_POINT%