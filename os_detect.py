import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys

def tcp(ip):
    packet = IP(dst=ip)/TCP(dport=80)
    response = sr1(packet, timeout=5, verbose=0)
    if response is None:
        return -2
    elif(response.haslayer(TCP)):
        return response.ttl
    else:
        -1

def os_detect(ip):
    sample_space = {60:"AIX",  254:"Solaris", 64:"Linux/Unix", 128:"Windows", 255:"Sun OS" }
    ttl_val = tcp(ip)
    print(ip," - ", sample_space[ttl_val])

def main():
    # print(len(sys.argv))
    if(len(sys.argv) != 2):
        print("Enter -- os_detect.py <IP>")

    ip = sys.argv[1]
    # ip = input("Enter IP: ")
    os_detect(ip)
    exit(0)

if __name__ == "__main__":
    main()
