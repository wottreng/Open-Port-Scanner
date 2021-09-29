import os
import time


class findHome:
    def __init__(self):
        self.scan: bool = True
        self.ranges: list = ["10.42.0.1/24", "192.168.1.1/24"]
        self.fileLocation: str = f"{os.getcwd()}/data.txt"
        self.data: str = ""
        self.dataLines: list = []
        self.ipAddressList: list = []

    def scanForOpenPort(self, range, port):
        print(f"Scanning range: {range}")
        tick = time.time()
        self.data = os.popen(f"nmap -p {port} {range}").read()
        print(f"time to scan: {time.time() - tick} sec")

    def writeToFile(self, output):
        with open(self.fileLocation, "a") as file:
            file.write(output)

    def readNMAPoutput(self):
        print("scanning file for open port...")
        with open(self.fileLocation, "r") as file:
            fileData = file.readlines()
        x = 0
        for line in fileData:
            if "open" in line:
                self.dataLines.append(x)
            x += 1
        for index in self.dataLines:
            self.ipAddressList.append(fileData[index - 4].split("(")[1].strip(")\n"))


if __name__ == '__main__':
    a = findHome()
    tick = time.time()
    if a.scan:
        for range in a.ranges:
            a.scanForOpenPort(range, "80")
            a.writeToFile(a.data)
    a.readNMAPoutput()
    print(a.ipAddressList)
    print('[*] done [*]')
    functTime = time.time() - tick
    print(f"function time: {functTime} sec")
    print(f"function time: {functTime / 60} min")
