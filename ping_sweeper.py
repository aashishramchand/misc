#! /usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

def alive_check(target):
    res = sr1(IP(dst=target)/ICMP(), timeout=10, verbose=0)
    if res is not None:
        print(target, " ===> is Up.")
    else:
        print(target, " --> is Down.")

def main():
    # print(len(sys.argv))
    if(len(sys.argv) !=2):
        print("ping_swpr.py <a.b.c.d-y")
        exit(0)

    dst_ip = sys.argv[1]
    res = dst_ip.split("-")
    temp = res[0].split(".")
    ntwrk_id = ".".join(temp[:-1])
    host_begin = temp[-1:]
    host_begin = int(host_begin[0])
    host_end = int(res[1])

    for i in range(host_begin, host_end+1):
        ip = ntwrk_id + "." + str(i)
        #print(ip)
        alive_check(ip)

if __name__ == '__main__':
    main()
