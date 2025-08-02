# File: main.py
# Written by: Angel Hernandez
# Description: Module 4: Portfolio Milestone
# Requirement(s):

# Step 1: Build the ItemToPurchase class with the following specifications:

# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)

# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0

# Method
#print_item_cost()

# Step 2: In the main section of your code, prompt the user for two items and create two objects of
# the ItemToPurchase class.

# Step 3: Add the costs of the two items together and output the total cost.

import os

class ItemToPurchase:
    item_name: str
    item_price: float
    item_quantity: int

    @property
    def name(self):
        return self.item_name

    @property
    def price(self):
        return self.item_price

    @property
    def quantity(self):
        return self.item_quantity

    def __init__(self, item_name = "None", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = {self.item_quantity * self.item_price}")

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 4 - Portfolio Milestone ***\n')

    try:
     total = 0
     items = []
     for i in range(2):
         print(f"\nItem {i + 1}")
         item_name = input("Enter the item name: ")
         price_name = float(input("Enter the item price: "))
         item_quantity = int(input("Enter the item quantity: "))
         items.append(ItemToPurchase(item_name, price_name, item_quantity))
     print("\nTOTAL COST")
     for item in items:
         total = total + (item.quantity * item.price)
         item.print_item_cost()
     print(f"Total: ${total}")
    except Exception as e:
        print(e)

if __name__ ==  '__main__': main()