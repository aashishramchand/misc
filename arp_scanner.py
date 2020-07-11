import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import time
import sys

def arp_scnr(ntwrk_id, host_begin, host_end):
    for host in range(host_begin, host_end):
        target = ntwrk_id + "." + str(host)
        res = sr1(ARP(pdst=target), timeout=5, verbose=0)
        # print(ls(res))
        if res is not None:
            print(target, " : ", res.hwsrc)
        else:
            print(target, " -- Unknown")

def main():
    #print(len(sys.argv))
    if len(sys.argv) != 2:
        print("arp_scanner.py <a.b.c.d-e IP Range>")
        exit(0)

    dst_ip = sys.argv[1]
    res = dst_ip.split("-")
    temp = res[0].split(".")
    ntwrk_id = ".".join(temp[:-1])

    host_begin = (temp[-1:])
    host_begin = int(host_begin[0])
    host_end = int(res[1])

    arp_scnr(ntwrk_id, host_begin, host_end)

if __name__ == "__main__":
    main()
