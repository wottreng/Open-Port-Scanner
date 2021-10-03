# Open-Port-Scanner
python script to check for open ports for a single ip address or ip range/CIDR

## How to use:
* all config goes in main.py
* choose port and fill out ip address range
* run main.py from command line
* found ip addresses will be printed to command line
* nmap results are stored in portScanData.txt in workingFiles directory

## library:
* CIDRtools: for ip address and CIDR manipulation
* fileTools: for reading and writing data to files
* portScanner: runs nmap and filters output for results
* colorText: for printing colorful command line outputs
