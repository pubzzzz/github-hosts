import time
from typing import List, Any, Tuple

import requests

_1S_AS_NS:int=10**9
_999S_AS_NS:int=999*_1S_AS_NS
def accessIpRootPathWebNanoSeconds(ipJ:str,sleepSeconds:float=0.1)->int:
    if sleepSeconds>0:
        print(f"sleep {sleepSeconds}s,",end="")
        time.sleep(sleepSeconds)
    begin:int=time.time_ns()
    url:str=f"http://{ipJ}"
    print(f"request {url}")
    try:
        __response:requests.models.Response=requests.get(url=url,timeout=7)
    except (requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError) as e:
        print(f"get error {e},drop this ip {ipJ}")
        return _999S_AS_NS
    # print(response.status_code)
    # if __response.status_code != HTTP_OK:
    #     print(f"get bad response.status_code  {__response.status_code},drop this ip {ipJ}")
    #     return _999S_AS_NS

    end:int=time.time_ns()
    delta_ns:int=end-begin
    print(f"debug:{delta_ns}ns,{delta_ns/_1S_AS_NS}s")
    return delta_ns


def findMiniValueWithIdx(ls:List[Any])->Tuple[int,Any]:
    assert ls is not None and len(ls)>0
    minIdx,min=0,ls[0]
    for k,eleK in enumerate(ls):
        if min>eleK:
            minIdx=k
    assert minIdx is not None
    return minIdx,min

OS_HOSTS_PATH_FOR_WINDOWS="c:/Windows/System32/drivers/etc/hosts"
# OS_HOSTS_PATH_FOR_WINDOWS="e:/tmp/hosts"  #only for develop
OS_HOSTS_PATH_FOR_LINUX="/etc/hosts"
def osHostPath()->str:
    import platform
    osName=platform.platform()
    #'Linux-5.15.0-56-generic-x86_64-with-glibc2.17'
    #'Windows-10-10.0.19041-SP0'
    if osName.startswith("Windows"):
        return OS_HOSTS_PATH_FOR_WINDOWS
    elif osName.startswith("Linux"):
        return OS_HOSTS_PATH_FOR_LINUX
    else:
        assert False,f"only support Windows and Linux, but current os is {osName}"

_EOL_N="\n"
_EOL_RN="\r\n"
def judgeEndOfLine(text:str)->str:
    if _EOL_RN in text:
        return _EOL_RN
    if _EOL_N in text:
        return _EOL_N

    return _EOL_RN


def nowHuman():
    import time,datetime
    datetime.datetime.now()
    now_human:str = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    return now_human

def nowForFileName():
    import time,datetime
    datetime.datetime.now()
    now_str:str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{now_str}.{time.time_ns()}ns"

_INDEX_NOT_FOUND:int=-1
def replaceOsHostFile(mark_begin:str, mark_end:str, hostTextReplacer:str):
    text:str=None
    now_human:str=nowHuman()
    hostPath:str=osHostPath()
    with open(hostPath, "r") as f:
        text=f.read()
    assert text is not None
    eOL:str=judgeEndOfLine(text)
    bi=text.find(mark_begin)
    ei=text.find(mark_end)
    hasMark:bool=bi!=_INDEX_NOT_FOUND and ei!=_INDEX_NOT_FOUND
    fresh:bool= (bi==_INDEX_NOT_FOUND or ei==_INDEX_NOT_FOUND)
    #mayBeEditByOther:bool= .....
    if hasMark or fresh:
        #{backup
        import time,shutil
        from pathlib import Path
        bkPath:Path=Path(f"{hostPath}.backup.{nowForFileName()}")
        shutil.copy(hostPath,bkPath.absolute())
        #}
        if hasMark:
            newText:str=f"{text[0:bi]}{eOL}{mark_begin}{eOL}#{now_human}{eOL}{hostTextReplacer}{eOL}{text[ei:]}{eOL}"
        if fresh:
            newText:str=f"{text}{mark_begin}{eOL}#{now_human}{eOL}{hostTextReplacer}{eOL}{mark_end}{eOL}"
        with open(hostPath, "w") as f:
            f.write(newText)


HTTP_OK:int=200
