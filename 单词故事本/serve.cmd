@echo off
rem ============================================================
rem  Word Storybook - local preview server (double-click me)
rem
rem  Serves THIS folder over http://127.0.0.1 so the page can load
rem  the sibling audio/ folder. Audio uses relative paths, and those
rem  only resolve when the page is opened through a real URL.
rem
rem  Extra arguments pass straight through, for example:
rem      serve.cmd --lan             also reachable from your phone
rem      serve.cmd --port 9000       start from another port
rem      serve.cmd --no-browser      do not auto-open the browser
rem ============================================================
chcp 65001 >nul
cd /d "%~dp0"
title Word Storybook - Preview

set "PY="

where py >nul 2>nul
if %errorlevel%==0 set "PY=py"
if not defined PY where python >nul 2>nul
if not defined PY if %errorlevel%==0 set "PY=python"

rem --- fallback: common per-user Python install locations ---
if not defined PY for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if not defined PY if exist "%%~fD\python.exe" set "PY=%%~fD\python.exe"
if not defined PY for /d %%D in ("%ProgramFiles%\Python3*") do if not defined PY if exist "%%~fD\python.exe" set "PY=%%~fD\python.exe"
if not defined PY if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" set "PY=%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe"

if not defined PY (
  echo.
  echo   Python not found on this machine.
  echo   Install it from https://www.python.org/downloads/
  echo   and tick "Add python.exe to PATH" during setup.
  echo.
  pause
  exit /b 1
)

"%PY%" "%~dp0serve.py" %*

if errorlevel 1 (
  echo.
  echo   Server exited with an error. Press any key to close.
  pause >nul
)
