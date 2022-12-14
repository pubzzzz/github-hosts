import time
from time import sleep
from typing import List, Tuple, Any

from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}#/html/body/div[1]/main/section[3]/div[2]/table/tbody/tr[6]/td/ul/li[1]
# ip_xpath:str="/html/body/div[1]/main/section[3]/div/table/tbody/tr[6]/td/ul/li[1]"
#/html/body/div[1]/main/section[2]/div[1]/table/tbody/tr[6]/td/ul/li[1]
ip_xpath:str="/html/body/div[1]/main/section/div/table/tbody/tr[6]/td/ul/li"
HTTP_OK:int=200
def fetch_ip(host:str)->str:
    """
    :param host:
        github.global.ssl.fastly.net
    :return:
    """

    url:str=f"https://www.ipaddress.com/site/{host}"
    while True:
        try:
            response:requests.models.Response=requests.get(url=f"https://www.ipaddress.com/site/{host}",headers=headers,timeout=1)
        except requests.exceptions.ReadTimeout as e:
            print(f"{url},{e},sleep 3s,continue")
            sleep(3)
            continue
        # print(response.status_code)
        if response.status_code != HTTP_OK:
            print(f"retry because http_response.status_code: {url}, {response.status_code}")
            continue
        response_text:str=response.text
        break

    dom:etree._Element=etree.HTML(response_text)
    _ls:List[etree._Element]=dom.xpath(ip_xpath)
    _text_ls:List[str]=list(map(lambda i:i.text,_ls))
    print(f"{url},{_text_ls}")
    return _text_ls

#https://www.ipaddress.com/site/github.global.ssl.fastly.net
# _1=fetch_ip("github.global.ssl.fastly.net")
#https://www.ipaddress.com/site/github.githubassets.com
# _2=fetch_ip("github.githubassets.com")

def httpIpRootPathNanoSeconds(ip:str)->int:
    time.sleep(1)
    begin:int=time.time_ns()
    requests.get(f"http://{ip}")
    end:int=time.time_ns()
    delta_ns:int=end-begin
    return delta_ns

def minWithIdx(ls:List[Any])->Tuple[int,Any]:
    pass

def iterateHostK(k, hostK, _ipKLs)->str:
    ipKLs=list(filter(lambda i:":" not in i,_ipKLs))  #clear ipv6 address
    if ipKLs is not None and len(ipKLs)>0:
        if len(ipKLs) == 1:
            return f"{ipKLs[0]}  {hostK}   "
        else:
            ns_ls:List[int]=[httpIpRootPathNanoSeconds(ipK) for i,ipK in enumerate(ipKLs)]
            i,_ns=minWithIdx(ns_ls)
            return f"{ipKLs[0]}  {hostK}  #{' '.join(ipKLs[1:])}"
    else:
        return f'#{hostK}'

if __name__=="__main__":
    host_ls:List[str]=[
        "github.githubassets.com",
        "central.github.com",
        "desktop.githubusercontent.com",
        "assets-cdn.github.com",
        "camo.githubusercontent.com",
        "github.map.fastly.net",
        "github.global.ssl.fastly.net",
        "gist.github.com",
        "github.io",
        "github.com",
        "api.github.com",
        "raw.githubusercontent.com",
        "user-images.githubusercontent.com",
        "favicons.githubusercontent.com",
        "avatars5.githubusercontent.com",
        "avatars4.githubusercontent.com",
        "avatars3.githubusercontent.com",
        "avatars2.githubusercontent.com",
        "avatars1.githubusercontent.com",
        "avatars0.githubusercontent.com",
        "avatars.githubusercontent.com",
        "codeload.github.com",
        "github-cloud.s3.amazonaws.com",
        "github-com.s3.amazonaws.com",
        "github-production-release-asset-2e65be.s3.amazonaws.com",
        "github-production-user-asset-6210df.s3.amazonaws.com",
        "github-production-repository-file-5c1aeb.s3.amazonaws.com",
        "githubstatus.com",
        "github.community",
        "media.githubusercontent.com",
        "objects.githubusercontent.com"
    ]
    ip_ls=[fetch_ip(hostK) for hostK in host_ls]

    line_ls=[iterateHostK(k, hostK, ip_ls[k]) for k,hostK in enumerate(host_ls)]
    text="\n".join(line_ls)
    with open("./hosts","w") as f: f.write(text)
    # print(text)
    end=True