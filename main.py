import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    suspicious_devices = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

        if element[1].hwsrc == "00:00:00:00:00:00":
            suspicious_devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc, "reason": "Zero MAC Address"})

    return clients_list, suspicious_devices

def print_result(results_list):
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

def print_suspicious_devices(devices_list):
    if devices_list:
        print("\nSuspicious Devices:")
        print("IP\t\t\tMAC Address\t\tReason")
        print("-----------------------------------------")
        for device in devices_list:
            print(device["ip"] + "\t\t" + device["mac"] + "\t" + device["reason"])

ip_range = "192.168.1.1/24"
scan_result, suspicious_devices = scan(ip_range)

print("Scanned Devices:")
print_result(scan_result)
print_suspicious_devices(suspicious_devices)
