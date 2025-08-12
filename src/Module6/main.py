# File: main.py
# Written by: Angel Hernandez
# Description: Module 6 - Portfolio Milestone
# Requirement(s):

import os
from shoppingCart import ShoppingCart
from itemToPurchase import ItemToPurchase

def clear_screen():
    # 'nt' means Windows, otherwise assume POSIX (*nix)
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    clear_screen()
    print('*** Module 6 - Critical Thinking ***\n')

def print_menu(cart):
    options = {
        'a': lambda: cart.add_item(ItemToPurchase(
            input("Enter the item name: "),
            input("Enter the item description: "),
            float(input("Enter the item price: ")),
            int(input("Enter the item quantity: "))
        )),
        'r': lambda: cart.remove_item(input("Enter name of item to remove: ")),
        'c': lambda: cart.modify_item(ItemToPurchase(
            input("Enter the item to modify: "),
            input("Enter the item description: "),
            float(input("Enter the item price: ")),
            int(input("Enter the item quantity: "))
        )),
        'i': lambda: (print("OUTPUT ITEMS' DESCRIPTIONS"), cart.print_descriptions()),
        'o': lambda: (print("OUTPUT SHOPPING CART"), cart.print_total()),
        'q': lambda: exit()
    }

    while True:
        print("\n*** MENU ***\n")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("\nChoose an option: ").lower()
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose again.")

try:
    clear_screen()
    print('*** Module 6 - Portfolio Milestone ***\n')
    current_cart = ShoppingCart("John Doe")
    print_menu(current_cart)
except Exception as e:
    print(e)

if __name__ == '__main__': main()