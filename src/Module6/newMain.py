# File: main.py
# Written by: Angel Hernandez
# Description: Module 6 - Portfolio Milestone
# Requirement(s):

import os

########################## ItemToPurchase Class ##########################

class ItemToPurchase:
    item_name: str
    item_price: float
    item_quantity: int
    item_description: str

    @property
    def name(self):
        return self.item_name

    @property
    def price(self):
        return self.item_price

    @property
    def quantity(self):
        return self.item_quantity

    @property
    def description(self):
        return self.item_description

    def __init__(self, item_name="None", item_description="", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = {self.item_quantity * self.item_price}")


##########################################################################

########################## ShoppingCart Class ############################

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.name == item_to_modify.name:
                found = True
                updates = {
                    'description': lambda: setattr(item, 'item_description', item_to_modify.item_description),
                    'price': lambda: setattr(item, 'item_price', item_to_modify.item_price),
                    'quantity': lambda: setattr(item, 'item_quantity', item_to_modify.item_quantity),
                }
                conditions = {
                    'description': item_to_modify.description != "none",
                    'price': item_to_modify.price != 0,
                    'quantity': item_to_modify.quantity != 0,
                }

                for key, condition in conditions.items():
                    if condition:
                        updates[key]()
                break

        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                total = item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price} = ${total}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        message = "Items Descriptions" if self.cart_items else "SHOPPING CART IS EMPTY - NO ITEMS"
        print(message)
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

##########################################################################

###################### Main and Support Methods ##########################

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

##########################################################################