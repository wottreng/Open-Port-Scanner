#!/usr/bin/python3
import time
from portScanner import portScanner
from CIDRtools import CIDRtools
from fileTools import fileTools
from colorText import colorText

CIDRlist = ["10.205.132.0/24"]

if __name__ == '__main__':
    ScanForPorts = True  # scan for open ports?
    # ----------
    portScanner = portScanner()
    CIDRtools = CIDRtools()
    fileTools = fileTools()
    colorText = colorText()
    # -----------
    startTime = time.time()
    # -----
    if not CIDRlist:
        CIDRlist = fileTools.readFileList(filename="workingFiles/cidrList.txt")
    scannedIPs = fileTools.readFileList(filename="workingFiles/scannedIP.txt")
    subCIDRlist = CIDRtools.buildSubCIDRlist(CIDRlist)
    fileTools.writeListToFile(subCIDRlist, filename="workingFiles/subCIDRlist.txt")
    if ScanForPorts:
        for ipaddr in subCIDRlist:
            if ipaddr not in scannedIPs:
                portScanOutput = portScanner.scanForOpenPort(ipaddr, port="80")
                fileTools.writeStrToFile(portScanOutput, filename="workingFiles/portScanData.txt", method="a")
                fileTools.writeStrToFile(ipaddr, filename="workingFiles/scannedIP.txt", method="a")
    ipResults = portScanner.readFileForOpenPorts(filename="workingFiles/portScanData.txt")
    colorText.printColorText("[*] function finished [*]", color="green", blink=False, underline=True, bold=False)
    if ipResults:
        colorText.printColorText(f"results: {ipResults}", color="blue", blink=False, underline=True, bold=False)
    else:
        colorText.printColorText("[*] port scan found no matches", color="red", blink=False, underline=False, bold=False)
    functTime = time.time() - startTime
    print(f"function time: {round(functTime, 2)} sec")
    print(f"function time: {round(functTime / 60, 2)} min")
