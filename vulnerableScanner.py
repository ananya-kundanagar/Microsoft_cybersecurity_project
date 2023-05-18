import portscanner
class vulnerablescan:
    def __init__(self,targetip,portnum,vul_file):
        self.target_ip = targetip
        self.portnum = portnum
        self.vul_file = vul_file

    def filesave(self):
        target = portscanner.portscan(self.target_ip, self.portnum)
        target.scan()
        with open(self.vul_file,'rt') as file:
            cout = 0
            for banner in target.banners:
                file.seek(0)
                for line in file.readline():
                    if line.strip() in banner:
                        print(f"Vulnerable Banner {banner} on port {str(target.open_port[cout])}")
                    cout +=1
