#!/usr/bin/env python3   # used if you want to run via cli Ex :. ./portScan.py
# PortScan Script Python
# @Author: Anderson Farias

import socket

host_target = input("Enter the host a scanned being (Ex:. www.domain.com or 192.168.1.1): ")
rangePort = input("Enter the range of ports to be scanned (Ex:. 1-1024): ")

print("scanning target: ", host_target)
print("scanning range: ", rangePort)
startPort = int(rangePort.split("-", 1)[-2])  # the variable receives the value before the "-"
endPort = int(rangePort.split("-", 1)[-1])    # the variable receives the value after the "-"

# checks if the values then fall within the range 1-65536
if (startPort > 65536 or endPort > 65536) or (startPort == 0 or endPort == 0):
    print("Invalid value, the port range allowed is 1-65536")
    exit()
# checks if the second value is greater than the first and inverts to form a range from largest to smallest    
elif startPort <= endPort:
    pass
else:
    startPort = int(rangePort.split("-", 1)[-1])
    endPort = int(rangePort.split("-", 1)[-2])

# checks if the first value is equal to the second, if truth does not need a loop
if startPort == endPort:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a socket for connection
    client.settimeout(0.5)  # timeout
    cod = client.connect_ex((host_target, startPort))  # set the target and the current portal to be scanned
    if cod == 0:
        portStatus: str = "Open"
    else:
        portStatus: str = "Close"
    print("Port:", startPort, "Status:", portStatus)
else:
    for i in range(startPort, endPort + 1, 1):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a socket for connection
        client.settimeout(0.5)  # timeout
        cod = client.connect_ex((host_target, i))  # set the target and the current portal to be scanned
        if cod == 0:
            portStatus: str = "Open"
        else:
            portStatus: str = "Close"
        print("Port:", i, "Status:", portStatus)

