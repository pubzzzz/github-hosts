from time import sleep
from typing import List

import requests
from lxml import etree

from util import HTTP_OK

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
"""test xpath for https://www.ipaddress.com/site/github.global.ssl.fastly.net
/html/body/div[1]/main/section[3]/div[2]/table/tbody/tr[6]/td/ul/li[1]
/html/body/div[1]/main/section[3]/div/table/tbody/tr[6]/td/ul/li[1]
/html/body/div[1]/main/section[2]/div[1]/table/tbody/tr[6]/td/ul/li[1]
"""
ip_xpath:str="/html/body/div[1]/main/section/div/table/tbody/tr[6]/td/ul/li"


def fetchIpFrom__www_ipaddress_com(host:str, timeoutSeconds:int=5, sleepGapSecondsWhenTimeout:int=3, maxReqCnt:int=7)->str:
    """
    :param host:
        github.global.ssl.fastly.net
    :return:
    """

    url:str=f"https://www.ipaddress.com/site/{host}"
    response_text: str =None
    for __ in range(maxReqCnt):
        try:
            response:requests.models.Response=requests.get(url=f"https://www.ipaddress.com/site/{host}",headers=headers,timeout=timeoutSeconds)
        except (requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError) as e:
            print(f"{url},{e},sleep {sleepGapSecondsWhenTimeout}s,continue")
            sleep(sleepGapSecondsWhenTimeout)
            continue
        # print(response.status_code)
        if response.status_code != HTTP_OK:
            print(f"retry because http_response.status_code: {url}, {response.status_code}")
            continue
        response_text=response.text
        break

    assert response_text is not None,"increase maxReqCnt? or you are offline?"

    dom:etree._Element=etree.HTML(response_text)
    _ls:List[etree._Element]=dom.xpath(ip_xpath)
    _text_ls:List[str]=list(map(lambda i:i.text,_ls))
    print(f"{url},{_text_ls}")
    return _text_ls


#test me:
# if __name__=="__main__":
#     host_ls:List[str]=fetch_ip_from__www_ipaddress_com("github.global.ssl.fastly.net")