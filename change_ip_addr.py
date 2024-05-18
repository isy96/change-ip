from os import name,system
import random


def change_ip_addr():
    choose_ip = random.randint(2, 254)
    choose_ip1 = random.randint(2, 254)

    if name == 'nt':
        print("this tool not for windows users")

    else:
        system(f'sudo ifconfig eth0 192.168.{choose_ip}.{choose_ip1}')



if __name__ == '__main__':
    while 1==1:
        change_ip_addr()