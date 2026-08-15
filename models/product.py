"""
PRE-WRITTEN CODE — DO NOT MODIFY THIS FILE
===========================================

This file contains the Product class used by the ShopSmart platform.
Read it to understand how it works — you will use it in other files.
"""


class Product:
    """Represents a product in the ShopSmart store."""

    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Product price cannot be negative")
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
