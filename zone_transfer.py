#!/usr/bin/python3
#oscp exercise

#!/usr/bin/python3

import subprocess
import time

domain_name=input("Enter the domain name i.e. google.com\n")

if(len(domain_name)<=0):
    print("*"*30)
    print("Domain field is empty")
else:
    print("*"*30)
    print("**Checking for Authorative name servrs*******")
    time.sleep(3)
    name_servers=subprocess.run(["host", "-t", "ns",domain_name])
    print(name_servers.stdout)
    print("*"*30)
    dns_servers=input("Enter the Authorative name servers for zone file transfer\n")
    zone_file=subprocess.run(["host", "-l", domain_name, dns_servers])
    print(zone_file.stdout)

