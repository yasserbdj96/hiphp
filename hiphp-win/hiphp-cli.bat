@echo off
rem   .                                                         .   
rem --+---------------------------------------------------------+-- 
rem   .    Code by: yasserbdj96                                 .   
rem   .    Email: yasser.bdj96@gmail.com                        .   
rem   .    GitHub: github.com/yasserbdj96                       .   
rem   .    Sponsor: github.com/sponsors/yasserbdj96             .   
rem   .    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9      .   
rem   .                                                         .   
rem   .    All posts with #yasserbdj96                          .   
rem   .    All views are my own.                                .   
rem --+---------------------------------------------------------+-- 
rem   .                                                         .   

rem START{
cls
Setlocal EnableDelayedExpansion

rem make symbels true:
for /F "tokens=2 delims=:" %%C in ('chcp') do set /A "$CP=%%C"
chcp 437 > nul

set mypath="%~dp0"

rem config.ini:
FOR /F "tokens=*" %%A IN ('type !mypath!"config.ini"') DO set %%A


set key=
set url=

rem Parse the command-line arguments
for %%i in (%*) do (
  if "%%i"=="--key" (
    set "key=%%~j"
  )
  if "%%i"=="--KEY" (
    set "key=%%~j"
  )
  if "%%i"=="--url" (
    set "url=%%~j"
  )
  if "%%i"=="--URL" (
    set "url=%%~j"
  )
)

cd ..
!python_default_path! main.py --key="%key%" --url="%url%"

rem }END.
