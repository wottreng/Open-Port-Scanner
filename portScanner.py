#!/usr/bin/python3
import os
import time
import ipaddress

class findHome:
    def __init__(self):
        self.scan:bool = True
        self.ranges: list = ["192.168.1.0/24", "10.42.0.0/24"]
        self.fileLocation: str = f"{os.getcwd()}/data.txt"
        self.data: str = ""
        self.dataLines: list = []
        self.ipAddressList: list = []
        self.susIPaddr: list = []
        self.scannedIPs: list = []

    def scanForOpenPort(self,range, port):
        print(f"Scanning ip: {range}")
        tick = time.time()
        self.data = os.popen(f"nmap -Pn -v -p {port} {range}").read() 
        print(f"time to scan: {time.time() - tick} sec")

    def writeToFile(self, output):
        with open(self.fileLocation,"a") as file:
            file.write(f"{output}\n")

    def recordScannedIP(self, ip):
        with open(f"{os.getcwd()}/scannedIP.txt","a") as file:
            file.write(f"{ip}\n")

    def readScannedIP(self):
        with open(f"{os.getcwd()}/scannedIP.txt","r") as file:
            self.scannedIPs = file.readlines()

    def scanFileForOpenPort(self):
        print("scanning file for open port...")
        with open(self.fileLocation, "r") as file:
            fileData = file.readlines()
        x=0
        for line in fileData:
            if "open" in line:
                self.dataLines.append(x)
            x+=1
        for index in self.dataLines:
            self.susIPaddr.append(fileData[index-4].split("(")[1].strip(")\n"))

    def getIPaddrFromCIDR(self, ipCIDR):
        set1 = ipaddress.ip_network(ipCIDR)
        ip_list = [str(ip) for ip in set1]
        for ipv4 in ip_list:
            self.ipAddressList.append(ipv4)


if __name__ == '__main__':
    a = findHome()
    tick = time.time()
    a.readScannedIP()
    if a.scan:
        for range in a.ranges:
            a.getIPaddrFromCIDR(range)
            # a.writeToFile(str(a.ipAddressList))
        for ipaddr in a.ipAddressList:
            if ipaddr not in a.scannedIPs:
                a.scanForOpenPort(ipaddr, "80")
                a.writeToFile(a.data)
                a.recordScannedIP(ipaddr)
    a.scanFileForOpenPort()
    print(a.susIPaddr)
    for ipAddr in a.susIPaddr:
        print(f"[*] request ip: {ipAddr}")
        os.system(f"curl {ipAddr}")
    print('[*] done [*]')
    functTime = time.time() - tick
    print(f"function time: {functTime} sec")
    print(f"function time: {functTime/60} min")
