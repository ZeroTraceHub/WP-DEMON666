#!/usr/bin/env python3
import os
import sys
import time
from termcolor import colored
from colorama import init

init()

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(colored("""
██╗    ██╗██████╗ ██╗  ██╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██║    ██║██╔══██╗██║  ██║╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║ █╗ ██║██████╔╝███████║ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   
██║███╗██║██╔═══╝ ██╔══██║ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
╚███╔███╔╝██║     ██║  ██║██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
 ╚══╝╚══╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
    𝙒𝙋𝙓𝙋𝙇𝙊𝙄𝙏 乂 𝙂𝙊𝘿 𝙏𝙊𝙊𝙇𝙆𝙄𝙏 - By: CIPHERNOVAX909 乂 NEXUS X909 """, "red"))

def menu():
    banner()
    print(colored("\n[1] WordPress Site Finder", "cyan"))
    print(colored("[2] WordPress Login Cracker", "cyan"))
    print(colored("[3] WordPress Login Checker", "cyan"))
    print(colored("[4] WordPress Shell Uploader", "cyan"))
    print(colored("[5] Exit", "cyan"))

    choice = input(colored("\nChoose an option: ", "yellow"))
    if choice == '1':
        os.system("python3 modules/wp_finder.py")
    elif choice == '2':
        os.system("python3 modules/wp_cracker.py")
    elif choice == '3':
        os.system("python3 modules/wp_checker.py")
    elif choice == '4':
        os.system("python3 modules/wp_shell.py")
    elif choice == '5':
        print(colored("Goodbye!", "green"))
        sys.exit()
    else:
        print(colored("Invalid option!", "red"))
        time.sleep(2)
        menu()

if __name__ == '__main__':
    while True:
        menu()