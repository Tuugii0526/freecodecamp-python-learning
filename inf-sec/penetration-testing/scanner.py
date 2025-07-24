import nmap
scanner= nmap.PortScanner()
print("Welcome,this is simple nmap automation tool")
ip_address=input("Please enter the ip address you want to scan:")
resp =input("""
            1) syn ack scan
            2) udp scan
            3) comprehensive scan
            """)
if resp=='1':
    scanner.scan(ip_address,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print('Ip status:',scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports: ",)
