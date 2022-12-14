from typing import List

from get_from_www_ipaddress_com import fetchIpFrom__www_ipaddress_com
from util import accessIpRootPathWebNanoSeconds, findMiniValueWithIdx, replaceOsHostFile


#https://www.ipaddress.com/site/github.global.ssl.fastly.net
# _1=fetch_ip("github.global.ssl.fastly.net")
#https://www.ipaddress.com/site/github.githubassets.com
# _2=fetch_ip("github.githubassets.com")

def findFastIp_in_IpListForHostK(k, hostK, _ipKLs)->str:
    ipKLs=list(filter(lambda i:":" not in i,_ipKLs))  #clear ipv6 address
    if ipKLs is not None and len(ipKLs)>0:
        if len(ipKLs) > 1:
            print(f"try find fast ip : {hostK}, {_ipKLs}")
            ns_ls:List[int]=[accessIpRootPathWebNanoSeconds(ipJ) for j,ipJ in enumerate(ipKLs)]
            j,_ns= findMiniValueWithIdx(ns_ls)
            print(f"{hostK}:fast ip is :in idx {j},{ipKLs[j]},{_ns/(10^6)}ms")
            return f"{ipKLs[j]}  {hostK}  #{' '.join([*ipKLs[0:j], *ipKLs[j+1:]])}"
        else: # len(ipKLs) == 1
            return f"{ipKLs[0]}  {hostK}   "
    else:
        return f'#{hostK}'

MARK=__file__
from host_list_config import host_ls
def main():
    ip_ls:List[str]=[fetchIpFrom__www_ipaddress_com(hostK) for hostK in host_ls]
    line_ls:List[str]=[findFastIp_in_IpListForHostK(k, hostK, ip_ls[k]) for k,hostK in enumerate(host_ls)]
    text="\n".join(line_ls)
    replaceOsHostFile(f"#{MARK}_begin",f"#{MARK}_end",hostTextReplacer=text)
    # print(text)

if __name__=="__main__":
    main()