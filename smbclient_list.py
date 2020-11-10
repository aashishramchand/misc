
#smbclient -N -L 10.10.10.191
#smbmap -H 10.10.10.191
#smbmap -u '' -p '' -H 10.10.10.191
#smbclient -N -L 10.10.10.191 --option='client min protocol-nt1'

from netaddr import *
import sys
import subprocess
from subprocess import Popen, PIPE
import os
from datetime import datetime

def smb_scan(ip):

	print("ok this works, so far")
	my_file = open("test_1.txt", 'w+')
	my_file.close()
	my_file = open("test_1.txt", 'a')
	ip = '10.10.10.191'
	for i in range(4):
		#main_cmd1 = Popen(["nmap", "-h"], stdout=PIPE)		
		#result = Popen(["grep", "oA"], stdin=main_cmd1.stdout, stdout=PIPE, universal_newlines=True)
		#main_cmd1.stdout.close()
		result = Popen(["smbclient", "-N", "-L", ip], stdout=PIPE, universal_newlines=True)
		output, errors = result.communicate()
		my_file.write(output)
		my_file.write('\n +++++++++-------++++++++ \n')
		my_file.write(errors)
		my_file.write('\n\n' + '######################----------------######################' + '\n\n')

	my_file.close()	

def sm2(ip_list):
	print('ok here we are')
	my_file = open('os_system_thing', 'W+')
	my_file.clos()
	my_file = open('os_system_thing', 'a')
	ip_list['10.10.10.192', '10.10.10.213']
	hosts = open('hosts', 'r')
	lisr = hosts.readlines()
	for i in lisr:
		
	

def main():
	smb_scan('127.0.0.1')

if __name__ == '__main__':
	main()
