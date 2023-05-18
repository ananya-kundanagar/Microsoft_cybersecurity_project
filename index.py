import passwordsniffer
import portscanner
import vulnerableScanner
import sshbruteforce
import arpspoofing
import passwordcracker
import backdoorserver

def index():
    print("Welcome To Cyber Security Project Index : \n")
    print("INDEX : \n")
    print("1)PORT SCANNER \n")
    print("2)VULNERABLE SCANNER \n")
    print("3)BRUTE FORCE - SSH \n")
    print("4)ARP SPOOFING \n")
    print("5)PASSWORD SNIFFING \n")
    print("6)PASSWORD CRACKING - DECODING OF PASSWORD \n")
    print("7)BACKDOOR ENTRY  \n")
    choice = int(input('Enter The Choice You want to select'))
    selectChoice(choice)


def selectChoice(choice):
    if choice == 1:
        target_ip = input('[+] Enter targets for scan: ')
        portnum = int(input('[+] Enter the amount of port you want to scan till: '))
        target = portscanner.portscan(target_ip, portnum)
        target.scan()
    elif choice == 2:
        target_ip = input('[+] Enter targets for scan: ')
        portnum = int(input('[+] Enter the amount of port you want to scan till: '))
        vul_file = input('[+] Enter path to the file with vulnerable software')
        work = vulnerableScanner.vulnerablescan(target_ip,portnum,vul_file)
        work.filesave()
    elif choice == 3:
        host = input('[+] target address : ')
        username = input('[+] SSH Username : ')
        input_file = input('[+] Password file: ')
        target = sshbruteforce.bruteforce(host,username,input_file)
        target.connect()
    elif choice == 4:
        target_ip = str(input("enter the target ip"))
        router_ip = str(input("Enter the router ip"))
        target = arpspoofing.arpspoof(target_ip,router_ip)
        target.connect()
    elif choice == 5:
        target_ip1 = str(input("enter the target ip"))
        router_ip1 = str(input("Enter the router ip"))
        target1 = arpspoofing.arpspoof(target_ip1, router_ip1)
        target1.connect()
        conn = passwordsniffer.passwordsnif()

    elif choice == 6:
        type_of_hash = str(input('Which type of hash you want to bruteforce ? '))
        file_path = str(input("Enter path to file to bruteforce with: "))
        hash_to_decrypt = str(input('Enter the hash value to Bruteforce:'))
        passwordcracker.conversion(type_of_hash,file_path,hash_to_decrypt)
    elif choice == 7:
        backdoorserver.server()
    else :
        print("Wrong Choice")


index()



