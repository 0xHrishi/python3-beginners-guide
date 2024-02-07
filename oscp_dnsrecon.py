#!/usr/bin/python3

import subprocess

domain_name=input("Enter the domain name such as google.com:\n")

if (len(domain_name)<=0):
    print("Domain name field is empty")
else:
    zone_transfer=subprocess.run(["dnsrecon", "-d" , domain_name, "-t", "axfr"],capture_output=True, text=True)
    print("*"*30)
    print(zone_transfer.stdout)
    print("*"*30)
