# File: shoppingCart.py
# Written by: Angel Hernandez
# Description: Module 6 - Portfolio Milestone (ShoppingCart class)
# Requirement(s):

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
