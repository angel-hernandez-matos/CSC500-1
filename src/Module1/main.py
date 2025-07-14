# File: main.py
# Written by: Angel Hernandez
# Description: Assignment for Critical Thinking - Module 1
# Requirement(s):
#
# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output.
#
# Also, subtract the two numbers to find the output.
#
# Part 2:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output.
# Also, divide num1/num2 to find the output.
#
# Compile and submit your pseudocode, source code, and screenshots of the application executing the code from parts 1 and 2,
# the results and GIT repository in a single document (Word is preferred).


import os
from typing import Optional

class Operation:
    name = ""
    function = None

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def performcalculation(self, first: Optional[float] = 0.0, second: Optional[float] = 0.0 ):
        num1 = num2 = 0.0

        try:
            if first == second and first == 0.0:
               num1 = float(input('Enter first number: '))
               num2 = float(input('Enter second number: '))
            else:
                num1 = first
                num2 = second
            print(f"{self.name} - Result is {self.function(num1, num2)}")
        except ValueError:
            print('Error parsing input. Please enter a number...')

        return num1, num2

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 1 ***\n')

    operations = [
        ("\nPart 1", [Operation("Add", lambda a, b: a + b), Operation("Subtract", lambda a, b: a - b)]),
        ("\nPart 2", [Operation("Multiply", lambda a, b: a * b), Operation("Divide", lambda a, b: a / b)]),
    ]

    for part, ops in operations:
        print(part)
        num1 = num2 = 0.0
        for op in ops:
            num1, num2  = op.performcalculation(num1, num2)

if __name__ ==  '__main__': main()