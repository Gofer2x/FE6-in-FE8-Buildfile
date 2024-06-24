REM got this from some link vesly posted. thanks! putting this here so i can properly credit.
@echo off
setlocal enabledelayedexpansion
set FILE_MATCH=*.txt

for /R "%~dp0" %%F in (%FILE_MATCH%) do (
  set OUT_FILE=%%~dF%%~pF%%~nF%.event
  echo Assembling "%%~nxF"...
  enumerate.py "%%~nxF" "!OUT_FILE!"
)

pause