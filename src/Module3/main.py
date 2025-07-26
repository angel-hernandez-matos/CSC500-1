# File: main.py
# Written by: Angel Hernandez
# Description: Critical Thinking Assignment - Module 3
# Requirement(s):
#
# Part 1:
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax.
# Display each of these amounts and the total price.

# Part 2:
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours)
# and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on
# a 24-hour clock when the alarm goes off.

import os
import subprocess
import sys

@staticmethod
def __ensure_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"Installing missing package: {package_name}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Package '{package_name}' was installed successfully.")

class AlarmCalculator:
    def calculate(self):
        format = input("Use 12-hour?: ").lower()
        apply_am_pm = True if format == "yes" else False
        current_time = int(input("Enter the current time (0-23): "))
        wait_time = int(input("Enter the number of hours to wait for the alarm: "))
        time_to_elapse = (current_time + wait_time) % 24 #24 hours in a day
        print(f"The alarm you just set up will go off at {self.__format_hours(self, time_to_elapse, apply_am_pm)}\n")

    @staticmethod
    def __format_hours(self, time_to_elapse, apply_am_pm = False):
        retval = time_to_elapse

        if apply_am_pm:
            period = "AM" if 0 <= time_to_elapse < 12 else "PM"
            hour_12 = time_to_elapse % 12
            hour_12 = 12 if hour_12 == 0 else hour_12
            retval = f"{hour_12}:00 {period}"

        return retval

class BillCalculator:
    selection=[]
    accumulated_price = 0

    def generate(self):
        self.__input_selection(self)
        print("Meals weren't ordered\n") if len(self.selection) == 0 else self.__calculate_and_print(self)

    @staticmethod
    def __calculate_and_print(self):
        tip = self.accumulated_price * 0.18
        tax = self.accumulated_price * 0.07
        total = self.accumulated_price + tip + tax

        print("\n*** Your bill ***")

        for a,b in self.selection:
            print(f"{a.replace('_', ' ')} \t- ${b:.2f}")

        print("*" * 20)
        print(f"\nFood charge: ${self.accumulated_price:.2f}")
        print(f"Tip (18%): ${tip:.2f}")
        print(f"Sales tax (7%): ${tax:.2f}")
        print(f"Total amount: ${total:.2f}")
        print("\n*** THANK YOU ***\n")

    @staticmethod
    def __input_selection(self):
        count = 0
        import inflect
        number_to = inflect.engine()
        print()
        while True:
            count = count + 1
            selection = input(f"Enter your  {number_to.ordinal(count)} meal and price (e.g.:, steak 12.5 or rice_and_chicken 20.30): ")

            if not selection.strip():
                break
            else:
                try:
                    meal, price = selection.split()
                    price = float(price)
                    self.accumulated_price = self.accumulated_price + price
                    self.selection.append((meal, price))
                except Exception as e:
                    print(e)


def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    __ensure_package("inflect") # let's download required packages (if missing)
    clear_screen()
    print('*** Module 3 - Critical Thinking ***\n')

    try:
      while True:
          print("*** Main Menu ***")
          print("1. Part 1 (Calculate total amount of a meal)")
          print("2. Part 2 (Alarm calculator)")
          selection = input("\nEnter your choice? (blank exits): ")

          if not selection.strip():
              break
          elif int(selection) == 1:
              bc = BillCalculator()
              bc.generate()
          else:
              ac = AlarmCalculator()
              ac.calculate()
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()