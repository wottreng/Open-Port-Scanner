#!/usr/bin/python3
import os
import ipaddress

class CIDRtools:

    def __init__(self):
        self.CIDRlist = ["10.42.0.0/24, 192.168.1.0/24"]
        self.totalList: list = []
        self.subCIDRlist: list = []

    def writeToFile(self, output):
        with open(f"{os.getcwd()}/subCIDRlist.txt", "w") as file:
            file.write(f"{output}\n")

    def getIPaddrFromCIDR(self, ipCIDR):
        # cidrx = '185.117.73.0/24'
        set1 = ipaddress.ip_network(ipCIDR)
        ip_list = [str(ip) for ip in set1]
        for ipv4 in ip_list:
            # print(ipv4)
            self.totalList.append(ipv4)

    def getSubCIDRlist(self):
        for ipaddress in self.totalList:
            if ".0" in ipaddress:
                self.subCIDRlist.append(f"{ipaddress}/24")
        print(self.subCIDRlist)

    def buildSubCIDRlist(self):
        for cidr in self.CIDRlist:
            self.getIPaddrFromCIDR(cidr)
        #self.writeToFile(str(a.totalList))
        self.getSubCIDRlist()
        self.writeToFile(a.subCIDRlist)

    def readSubCIDRlist(self):
        with open(f"{os.getcwd()}/subCIDRlist.txt", "r") as file:
            data = file.readline()
        list = data.split(", ")
        for line in list:
            self.subCIDRlist.append(line.strip().strip("\'"))
        print(self.subCIDRlist)

if __name__ == '__main__':
    a = CIDRtools()
    a.getSubCIDRlist()


