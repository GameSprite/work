@echo off
setlocal enableDelayedExpansion

set /p zipspath=输入要处理的压缩包文件目录:
if not exist %zipspath% (
  echo %zipspath%不存在
   pause
) 
::zipssort
set fnum=0
for /f  %%A   in ('dir  /b/on  %zipspath%')  do (
  set /a fnum+=1
  set zfiles!fnum!=%%A
)
set /a temp=!fnum!
set temp=!zfiles%temp%!
::generate folder name which contains zip files
set timestr=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
set /a num_1=%temp:~4,2%
set zipsout_deals=%timestr%_%num_1%.%temp:~7,2%
echo %zipsout_deals%
::unzipandcombine
if exist %zipspath%\..\%zipsout_deals% rd /s/q %zipspath%\..\%zipsout_deals%
set /a flen=!fnum!
set /a endi=!fnum!-1
for /l %%i in (1,1,%endi%) do (
  set fnP=!zfiles%%i:~0,3!
  set /a fn1=!zfiles%%i:~4,2!+0
  set fnA=!fn1!.!zfiles%%i:~7,2!
  set /a fn2=!zfiles%flen%:~4,2!
  set fnB=!fn2!.!zfiles%flen%:~7,2!
  set zdir=%zipspath%\..\%zipsout_deals%\!fnP!_!fnA!_!fnB!

  if exist !zdir! rd /s/q !zdir!
  md !zdir!

  for /l %%j in (%%i,1,!fnum!) do (
    unzip -o %zipspath%\!zfiles%%j! -d !zdir!
  )
)

::zip
set zd=%zipspath%\..\%zipsout_deals%
%zd:~0,2%
cd %zd%
for /f %%Z in ('dir /b /ad-h %zd%') do (
  cd %%Z
  zip -r ..\%%Z.zip .\*
  cd ..\
  rd /s/q %%Z
)
pause