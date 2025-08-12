# File: itemToPurchase.py
# Written by: Angel Hernandez
# Description: Module 6 - Portfolio Milestone (ItemToPurchase class)
# Requirement(s):

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