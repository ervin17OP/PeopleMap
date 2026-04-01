@echo off
setlocal
if "%~1"=="" (
  echo Usage: scripts\git-push.cmd branch-name
  exit /b 1
)
powershell -ExecutionPolicy Bypass -File "C:\Users\ervin\PeopleMap\scripts\git-push.ps1" -Branch "%~1"
endlocal
