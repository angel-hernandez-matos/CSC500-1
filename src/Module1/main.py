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

add = lambda a, b: a + b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

def main():
    os.system('cls')
    print(' *** Module 1 *** \nPart 1\n')

    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f"Result is {add(num1, num2)}" )
        print('\nPart 2\n')
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f"Result is {multiply(num1, num2)}" )
        print(f"Result is {divide(num1, num2)}")
    except ValueError:
        print('Please enter a number\nExiting now...')

if __name__ ==  '__main__': main()