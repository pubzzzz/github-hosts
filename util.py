import time
from typing import List, Any, Tuple

import requests


def accessIpRootPathWebNanoSeconds(ipJ:str)->int:
    time.sleep(0.1)
    begin:int=time.time_ns()
    requests.get(f"http://{ipJ}")
    end:int=time.time_ns()
    delta_ns:int=end-begin
    return delta_ns


def findMiniValueWithIdx(ls:List[Any])->Tuple[int,Any]:
    assert ls is not None and len(ls)>0
    minIdx,min=0,ls[0]
    for k,eleK in enumerate(ls):
        if min>eleK:
            minIdx=k
    assert minIdx is not None
    return minIdx,min
