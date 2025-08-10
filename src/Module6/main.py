# File: main.py
# Written by: Angel Hernandez
# Description: Module 6 - Critical Thinking
# Requirement(s):

import os

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 6 - Critical Thinking ***\n')

    try:
     pass
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()