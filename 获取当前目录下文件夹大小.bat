@echo off 
echo calculating......
cd /d %~dp0
if exist %~dp0\\foldersize.txt (
   del %~dp0\\foldersize.txt
)
for /f "delims=" %%i in ('dir /ad-r-h-s /b') do (call :rename "%%i")
echo calculate end
exit
:rename
setlocal enabledelayedexpansion
set "folder=%1"
set size_M=0
set size_K=0
set num=0
for /f "tokens=* delims=" %%i in ('dir /a-d /b /s "%folder%"') do set /a num+=%%~zi
set /a size_K=%num%/1024
set /a size_M=%size_K%/1024
echo %folder% (%size_M%M,%size_K%K) >> %~dp0\\foldersize.txt
::ren "%~f1" "%folder%"%a%M