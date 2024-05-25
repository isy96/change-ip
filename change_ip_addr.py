from os import name,system
import random
import netifaces as ni
import time


def clear():
    if name == 'nt':
        system("cls")
    else:
        system("clear")

clear()

red = "\033[91m"

def get_interfaces():
    interfaces = ni.interfaces()
    return interfaces


def get_ip(interface):
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    return ip

def get_mask(interface):
    mask = ni.ifaddresses(interface)[ni.AF_INET][0]['mask']
    return mask





change_random = random.randint(2,254)
change_random1 = random.randint(2,254)




iface = get_interfaces()

count = 1

for i in iface:
    print(count , '-' , i)
    count += 1

user = ''


while not user.isdigit() or int(user.strip()) > count:
    user = input("enter interface : ")



user_choose = iface[int(user.strip()) -1] 

ip_addr = get_ip(user_choose)
subnet = get_mask(user_choose)

print('interface name : ' + iface[int(user) -1])
print('ip address : ' + ip_addr)
print('subnetmask : ' + subnet)


type_to_user = f"""
{red}to change type interface name like eth0 or lo 
"""
print(type_to_user)

user = input("enter interface name you want to change ip : " + str(iface) + '\n')



def change_ip():
    change_1 = random.randint(2,254)
    change_2 = random.randint(2,254)
    ask = system(f'sudo ifconfig {user} 192.168.{change_1}.{change_2}')
    if name == 'nt':
        print('error')

    else:
        print(f'192.168.{change_1}.{change_2}')

if __name__ == '__main__':
    with open("changed_ips.txt", "a") as file:
        while True:
            new_ip = change_ip()
            if new_ip:
                file.write(f'{new_ip}\n')
            time.sleep(1)
