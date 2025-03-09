@echo off
setlocal

:: Get the current script directory
set SCRIPT_DIR=%~dp0

:: Generate a unique virtual environment name based on the computer name
set ENV_DIR=%SCRIPT_DIR%.venv_%COMPUTERNAME%

:: Check if the virtual environment exists
if exist "%ENV_DIR%" (
    echo ✅ Virtual environment already exists at: %ENV_DIR%
    echo 👉 To activate it, run:
    echo    call %ENV_DIR%\Scripts\activate
    exit /b 0
) else (
    echo Creating new virtual environment in: %ENV_DIR%
    python -m venv "%ENV_DIR%"
)

:: Activate the virtual environment
call "%ENV_DIR%\Scripts\activate"

:: Upgrade pip, setuptools, and wheel
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

:: Install required ML packages
echo Installing ML libraries...
python -m pip install --no-cache-dir ^
    numpy ^
    pandas ^
    matplotlib ^
    scikit-learn ^
    scipy ^
    seaborn ^
    jupyter ^
    ipython ^
    notebook

:: Deactivate the virtual environment
deactivate

:: Print activation message
echo ✅ Setup complete!
echo 👉 To start using the environment, run:
echo    call %ENV_DIR%\Scripts\activate

endlocal
