@ECHO OFF

SET MYPATH=%~dp0
SET MYSCRIPT=%MYPATH%\utils\today\main.py 

python3 %MYSCRIPT% %1

pause