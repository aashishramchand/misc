import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import time
import sys

def udp_scnr(target, start, end):
    for port in range(start, end):
        res = sr1(IP(dst=target)/UDP(dport=port), timeout=5, verbose=0)
        # print(res)
        if res is None:
            print(port, " is Open")
        else:
            print(port, " is Closed")


def main():
    #print(len(sys.argv))
    if len(sys.argv) != 4:
        print(" Enter IP A-B (port-range)")
        exit(0)

    target = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    udp_scnr(target, start, end)

if __name__ == "__main__":
    main()
