#!/usr/bin/python3
import os
import ipaddress

class CIDRtools:

    def __init__(self):
        self.testCIDR = ["10.42.0.0/23"]

    def writeToFile(self, data: list, fileName: str = "CIDRtoolsOutput.txt"):
        with open(f"{os.getcwd()}/{fileName}", "w") as file:
            for line in data:
                file.write(f"{line}\n")

    def getAllIPaddrFromCIDR(self, ipCIDR: str):
        # ipCIDR = '185.117.73.0/24'
        allIPaddresses: list = []
        set1 = ipaddress.ip_network(ipCIDR)
        ip_list = [str(ip) for ip in set1]
        for ipv4 in ip_list:
            # print(ipv4)
            allIPaddresses.append(ipv4)
        return allIPaddresses

    def getSubCIDRlist(self, allIPaddresses: list):
        subCIDRlist: list = []
        for ipaddress in allIPaddresses:
            if ".0" in ipaddress[-2:]:
                subCIDRlist.append(f"{ipaddress}/24")
        return subCIDRlist

    def buildSubCIDRlist(self, CIDRlist: list):
        # CIDRlist = ["1.1.1.0/19","etc..."]
        allSubCIDRs: list = []
        for CIDR in CIDRlist:
            allIPaddresses = self.getAllIPaddrFromCIDR(CIDR)
            subCIDRlist = self.getSubCIDRlist(allIPaddresses)
            for CIDR in subCIDRlist:
                allSubCIDRs.append(CIDR)
        return allSubCIDRs

    def readSubCIDRlist(self, fileName: str = "allSubCIDRs.txt"):
        CIDRlist: list = []
        with open(f"{os.getcwd()}/{fileName}", "r") as file:
            data: list = file.readlines()
        for line in data:
            CIDRlist.append(line.strip())
        return CIDRlist

if __name__ == '__main__':
    a = CIDRtools()
    allSubCIDRs = a.buildSubCIDRlist(a.testCIDR)
    print(allSubCIDRs)
    a.writeToFile(allSubCIDRs, "allSubCIDRs.txt")
    CIDRlist = a.readSubCIDRlist()
    print(CIDRlist)
