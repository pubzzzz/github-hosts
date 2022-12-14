@echo off
SET script_dir=%~dp0
cd /d %script_dir%

where python
IF %ERRORLEVEL% NEQ 0 (
    echo "exit,because:python not found. please insert python3 ,then set it to env PATH"
    pause
    exit 2
)

python -c "print('this is python3')"

IF %ERRORLEVEL% NEQ 0 (
    echo "exit,because:python2 found but python3 not found. please insert python3 ,then set it to env PATH"
    pause
    exit 4
)

pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    echo "exit,because:pip dependency install failed. please run github_hosts_fetch.py manual"
    pause
    exit 6
)
echo "environment is ok, now run github_hosts_fetch.py"
python github_hosts_fetch.py && echo "ok,now you can access https://github.com at your browser"
explorer https://www.github.com
pause