# File: main.py
# Written by: Angel Hernandez
# Description: Module 5: Critical Thinking
# Requirement(s):
#
# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user
# for the inches of rainfall for that month. After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

# Part 2:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased
# each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then
# display the number of points awarded.

import os

class PartOne:
    @staticmethod
    def collect_and_calculate_rainfall_data():
        total_rainfall = 0.0
        total_months = 0
        print("\n=== PART 1 ===")
        years = int(input("Enter the number of years?: "))

        # Outer loop (iterate over each year)
        for year in range(1, years + 1):
            print(f"\nYear {year}")
            # Inner loop (iterate over each month)
            for month in range(1, 13):
                while True:
                    try:
                        rainfall = float(input(f"Enter rainfall (in inches) for month {month}?: "))
                        if rainfall < 0:
                            print("Rainfall cannot be negative. Please enter a valid number.")
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                # Update totals
                total_rainfall += rainfall
                total_months += 1

        # Calculate average rainfall
        average_rainfall = total_rainfall / total_months

        # Display summary
        print("\n*** Rainfall Summary ***")
        print(f"Total months: {total_months}")
        print(f"Total rainfall: {total_rainfall:.2f} inches.")
        print(f"Monthly Average Rainfall: {average_rainfall:.2f} inches.")

class PartTwo:
    @staticmethod
    def calculate_award_points():
        points_lookup = {
            0: lambda: 0,
            2: lambda: 5,
            4: lambda: 15,
            6: lambda: 30
        }

        print("\n=== PART 2 ===")
        try:
            books_purchased = int(input("Enter the number of books you purchased this month?: "))
            if books_purchased < 0:
                print("Number of books cannot be negative.\n")
                return

            points = points_lookup.get(books_purchased,
                                       lambda: 60 if books_purchased >= 8 else 0)()
            print(f"You have earned {points} points this month.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 5 - Critical Thinking ***\n')
    try:
        PartOne.collect_and_calculate_rainfall_data()
        PartTwo.calculate_award_points()
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()