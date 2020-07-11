'''POrt Scanner'''
#! /usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

def sscan(target, d_port, src_port):
    res = sr1(IP(dst=target)/TCP(dport=d_port,flags="S"),timeout=5, verbose=0)
    #print(res)
    if(res is None):
        print("Filtered")
    elif(res.getlayer(TCP)):
        if(res.getlayer(TCP).flags == 0x12):
            temp_res = sr(IP(dst=target)/TCP(dport=d_port, flags="R"), timeout=5, verbose=0)
            print("Port ", d_port, " is Open")
        if(res.getlayer(TCP).flags == 0x14):
            print("Port is ", d_port, "is closed")
    elif(res.haslayer(ICMP)):
        print(int(res.getlayer(ICMP).type))
        if((int(res.getlayer(ICMP).type) == 3) and (int(res.getlayer(ICMP).code) in [1,2,3,9,10,13])):
            print("Port is Filtered")

def main():
    if(len(sys.argv) != 3):
        print("port_scanner <IP> <port-range a-b>")
        exit(0)

    target = sys.argv[1]
    port_range = sys.argv[2].split("-")
    # target = input("Enter IP: ")
    # port_range = input("Enter Port Range(a-b): ").split("-")
    d_port1, d_port2 = int(port_range[0]), int(port_range[1])
    src_port = RandShort()
    for d_port in range(d_port1, d_port2+1):
        #print(d_port)
        sscan(target, d_port, src_port)
    exit(0)
#
# def main():
#     target = raw_input("Enter IP: ")
#     d_port = raw_input("Enter Port Range(a-b): ").split("-")
#     #d_port = int(d_port)
#     d_port1, d_port2 = int(d_port[0]), int(d_port[1])
#     src_port = RandShort()
#     for port in range(d_port1, d_port2+1): print(port)
#
#     exit(0)
#     sscan(target, d_port, src_port)
#
#     arget = raw_input("Enter IP: ")
# 	d_port = raw_input("Enter Port Range(a-b): ").split("-")
# 	src_port = RandShort()
# 	d_port1, d_port2 = d_port[0], d_port[1]
# 	xmas_scan(target, d_port1, d_port2, src_port)

if __name__ == "__main__":
	main()
