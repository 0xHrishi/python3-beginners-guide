#!/usr/bin/python3

import subprocess
import time

domain_name=input("Enter the domain name i.e. google.com\n")

if (len(domain_name)<=0):
    print("*"*50)
    print("Domain field is empty")
else:
    print("******Zone file transfer using DNSRECON*****")
    time.sleep(5)
    dnsrecon=subprocess.run(["dnsrecon", "-d", domain_name, "-t", "axfr"])
    print(dnsrecon.stdout)
