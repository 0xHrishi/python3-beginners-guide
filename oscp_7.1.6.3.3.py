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

------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

import subprocess
import time

domain=input("Enter the domain name\n")

if (len(domain)==0):
    print("*"*50)
    print("Domain field empty")
else:
    print("*******Attempting zone file transfer using dnsrecon*******")
    time.sleep(2)
    zone_transfer=subprocess.run(["dnsrecon", "-d", domain, "-t", "axfr"], capture_output=True,text=True)
    print("*"*30)
    print(zone_transfer.stdout)
    print("*"*30)
    
