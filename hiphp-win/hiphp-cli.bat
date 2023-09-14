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
rem cls
setlocal EnableDelayedExpansion

rem Make symbols true:
for /F "tokens=2 delims=:" %%C in ('chcp') do set /A "$CP=%%C"
chcp 437 > nul

set "mypath=%~dp0"

rem Read config.ini and set variables:
FOR /F "tokens=*" %%A IN ('type "%mypath%config.ini"') DO set %%A

set "key="
set "url="
set "y="

:parse_args
if "%~1" == "" goto done_args

if /I "%~1" == "--key" (
  set "key=--key=%~2"
  shift
)
if /I "%~1" == "--url" (
  set "url=--url=%~2"
  shift
)
if /I "%~1" == "--y" (
  set "y=--y"
  shift
)
if /I "%~1" == "--proxies" (
  set "proxies=--proxies=%~2"
  shift
)
shift
goto parse_args

:done_args

cd ..

!python_default_path! main.py %url% %key% %y% %proxies%

rem }END.
