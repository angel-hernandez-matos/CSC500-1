# File: mainDiscussionForum.py
# Written by: Angel Hernandez
# Description: Code snippet for discussion forum - Module 6
# Requirement(s):
#
# Insert, update and delete operations on list and dictionary

import os

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def reverse_string(string):
    return ''.join(reversed(string))

def main():
    clear_screen()
    print('*** Module 6 - Discussion Forum ***\n')

    # Basic List
    names = ['Angel', 'Sara', 'Andre']

    # Combined List
    combined = [
        'This is a string',
        list(filter(lambda x: x % 2 == 0, range(1, 101))),
        reverse_string,
        {"Name": "Angel", "Surname": "Hernandez"}
    ]

    # Insert
    months = ['February', 'March', 'April']
    months.insert(0, 'January')  # Inserts at index 0
    student = {'Name': 'Angel', 'Surname': 'Hernandez'}
    student['Nationality'] = 'Australia'

    # Update
    months[0] = 'Enero' # January in Spanish
    student['Nationality'] = 'Australia/Venezuela'

    # Delete
    months.remove('April')
    del months[2]
    popMonth = months.pop()
    del student['Nationality']
    removed = student.pop('Surname')

    # Print Months and Student
    for month in months:
        print(month)

    for student in student.values():
        print(student)

   # Print different objects in list (and run code if present)
    for i in combined:
        print(i)
        if callable(i):
            print([i(x) for x in names]) # List comprehension to call our function pointer (callback)

if __name__ ==  '__main__': main()