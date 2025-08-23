# File: mainCT7.py
# Written by: Angel Hernandez
# Description: Module 7 - Critical Thinking
# Requirement(s):

import os
from enum import Enum, auto

class DictionaryType(Enum):
    ROOM_NUMBERS = auto()
    INSTRUCTORS = auto()
    MEETING_TIMES = auto()

class CourseInformation:
    __room_numbers__ = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    __instructors__ = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    __meeting_times__ = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    __data__ = {
        DictionaryType.ROOM_NUMBERS: __room_numbers__,
        DictionaryType.INSTRUCTORS: __instructors__,
        DictionaryType.MEETING_TIMES: __meeting_times__
    }

    def print_menu(self):
        options = {
            'r': lambda: self.__print_dictionary__(DictionaryType.ROOM_NUMBERS),
            'i': lambda: self.__print_dictionary__(DictionaryType.INSTRUCTORS),
            'm': lambda: self.__print_dictionary__(DictionaryType.MEETING_TIMES),
            's': lambda: self.__search_course__(input("Enter a course number (e.g., CSC101): ").strip().upper()),
            'q': lambda: exit()
        }

        while True:
            print("\n*** MENU ***\n")
            print("r - Output Room Numbers")
            print("i - Output Instructors")
            print("m - Output Meeting Times")
            print("s - Search for a course")
            print("q - Quit")

            choice = input("\nChoose an option: ").lower()
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please choose again.")

    def __search_course__(self, course):
        if course in self.__room_numbers__:
            print(f"Course: {course}")
            print(f"Room Number: {self.__room_numbers__[course]}")
            print(f"Instructor: {self.__instructors__[course]}")
            print(f"Meeting Time: {self.__meeting_times__[course]}")
        else:
            print("Course not found.")

    def __print_dictionary__(self, _type):
        for key, value in self.__data__[_type].items():
            print(f"{key}: {value}")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 7 - Critical Thinking ***\n')
try:
     ci = CourseInformation()
     ci.print_menu()
except Exception as e:
    print(e)

if __name__ == '__main__': main()