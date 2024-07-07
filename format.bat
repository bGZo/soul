@ECHO OFF


SET MYPATH=%~dp0
SET MYSCRIPT=%MYPATH%\utils\format\regex\main.py 
SET PYTHON_REQUIREMENT=%MYPATH%\utils\format\regex\requirements.txt

set http_proxy=http://127.0.0.1:7890
set https_proxy=http://127.0.0.1:7890

python3.exe -m pip install --trusted-host pypi.tuna.tsinghua.edu.cn -i https://pypi.tuna.tsinghua.edu.cn/simple -r %PYTHON_REQUIREMENT%
python3 %MYSCRIPT% %1

pause