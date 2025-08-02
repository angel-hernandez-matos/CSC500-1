# File: mainDiscussionForum.py
# Written by: Angel Hernandez
# Description: Code snippet for discussion forum - Module 4
# Requirement(s):
#
# Kill a given process based on user selection

import os
import subprocess
import sys

def __ensure_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"Installing missing package: {package_name}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Package '{package_name}' was installed successfully.")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def __process_handler():
    import psutil
    processes = [(p.pid, p.name()) for p in psutil.process_iter(attrs=["pid", "name"])]

    # Display the processes
    for pid, name in processes:
        print(f"PID: {pid}, Name: {name}")

    process_name = input("Process name you'd like to terminate: ")

    for proc in psutil.process_iter(attrs=["pid", "name"]):
        if proc.info["name"].lower() == process_name.lower():
            print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})")
            psutil.Process(proc.info["pid"]).terminate()
            break

def main():
    __ensure_package("psutil") # let's download required packages (if missing)
    clear_screen()
    print('*** Module 4 - Discussion Forum ***\n')
    try:
      __process_handler()
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()