pip install requests

#write ./hosts
python github_hosts_fetch.py
mv /etc/hosts /etc/hosts.orginal && cp ./hosts /etc/hosts