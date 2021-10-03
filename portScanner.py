import os
import time


class portScanner:

    def __init__(self):
        from colorText import colorText
        self.colorText = colorText()

    def scanForOpenPort(self, ipAddr, port: str = "80"):
        # ipAddr can be single ip address or cidr notation
        print(f"Scanning ip: {ipAddr}")
        tick = time.time()
        portScanOutput = os.popen(f"nmap -v -p {port} {ipAddr}").read()  # sS TCP SYN scan
        print(f"time to scan: {round(time.time() - tick, 2)} sec")
        return portScanOutput

    def readFileForOpenPorts(self,path=os.getcwd(), filename: str = "data.txt"):
        print("scanning file for open port...")
        results: list = []
        ipAddrList: list = []
        try:
            with open(f"{path}/{filename}", "r") as file:
                fileData = file.readlines()
            for line in fileData:
                if "Discovered open port" in line:
                    # print(line)
                    results.append(line.strip())
        except:
            self.colorText.printColorText(f"[*] file not found: {filename}", color="red", blink=False, underline=True, bold=True)
        for line in results:
            ipAddrList.append(line.split(" on ")[1])
        return ipAddrList

