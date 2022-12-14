#!/bin/bash
which python || (echo "exit,because:python not found. please insert python3 ,then set it to env PATH"; exit 2)
python -c "print('this is python3')" || (echo "exit,because:python2 found but python3 not found. please insert python3 ,then set it to env PATH"; exit 4)
pip install -r requirements.txt|| (echo "exit,because:pip dependency install failed. please run github_hosts_fetch.py manual"; exit 4)
echo "environment is ok, now run github_hosts_fetch.py"
cd ./fetch_ip_for_host/
python github_hosts_fetch.py && echo "ok,now you can access https://github.com at your browser"