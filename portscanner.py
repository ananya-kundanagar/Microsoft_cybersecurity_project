import socket
from IPy import IP

class portscan():
    banners = []
    open_port = []
    def __init__(self,target,port_num):
        self.target = target
        self.port_num = port_num

    def scan(self):
        #converted_ip=self.check_ip(self.target)
        #print('\n' + '[- 0 Scanning Target]' +str(self.target))
        for port in range(1,self.port_num):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self,port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip,port))
            self.open_port.append(port)
            try:
                banner1 = sock.recv(1024.).decode().strip('\n').strip('\r')
                self.banners.append(banner1)
                print('[+] Open Port' + str(port) + ' : ' +str(self.banner.decode().strip('\n')))
            except:
                self.banners.append(" ")
                print('[+] Open Port' +str(port))
        except:
        # print('[-] Port' + str(port) + 'Is Closed')
            pass





