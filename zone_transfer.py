#!/usr/bin/python3
#oscp exercise

import subprocess
domain=input("Enter the domain name such as google.com:\n")
name_server=input("Enter the name server :\n")


if (len(domain)<=0) or (len(name_server)<=0):
    if (len(domain)>0) and (len(name_server)<=0):
        print("Name server field is empty")
    elif (len(domain)<=0) and (len(name_server)>0):
        print("Domain field is empty")
    else:
        print("Issues with the user input")

elif (len(domain)>0) and (len(name_server)>0):
    zone_transfer=subprocess.run(["host", "-l", domain, name_server],capture_output=True, text=True)
    print("*" * 30)
    print(zone_transfer.stdout)
    print("*" * 30)
