"""
TODO 4a & 4b: Complete the ShoppingCart class
==============================================

This file contains a PARTIALLY written ShoppingCart class.
Some methods are already complete (DO NOT MODIFY those).
Your job is to implement the two methods marked with TODO.

Read the entire class first to understand what already exists,
then complete TODO 4a and TODO 4b at the bottom.
"""

from typing import Optional
from models.product import Product
from strategies.discount_strategy import DiscountStrategy


class ShoppingCart:
    """
    A shopping cart that holds products and can apply a discount
    strategy to calculate the final price.

    PRE-WRITTEN METHODS (DO NOT MODIFY):
      - __init__
      - add_item
      - remove_item
      - get_total
      - get_item_count

    YOUR METHODS (TODO):
      - set_discount_strategy  (TODO 4a)
      - calculate_final_price  (TODO 4b)
    """

    def __init__(self):
        self._items = []
        self._discount_strategy: Optional[DiscountStrategy] = None

    def add_item(self, product: Product):
        """Add a product to the cart."""
        self._items.append(product)

    def remove_item(self, product_name: str):
        """Remove the first product with the given name from the cart.

        Raises ValueError if the product is not found.
        """
        for i, item in enumerate(self._items):
            if item.name == product_name:
                self._items.pop(i)
                return
        raise ValueError(f"Product '{product_name}' not found in cart")

    def get_total(self) -> float:
        """Return the total price of all items in the cart."""
        return sum(item.price for item in self._items)

    def get_item_count(self) -> int:
        """Return the number of items in the cart."""
        return len(self._items)

    # ==========================================================
    # TODO 4a: Implement set_discount_strategy
    # ==========================================================
    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Set or swap the discount strategy for this shopping cart.

        Args:
            strategy (DiscountStrategy): The discount strategy to use.
        """
        # TODO 4a: Store strategy in self._discount_strategy
        pass

    # ==========================================================
    # TODO 4b: Implement calculate_final_price
    # ==========================================================
    def calculate_final_price(self) -> float:
        """Calculate the final price of the cart after applying discount strategy.

        If no discount strategy is set, returns the cart total.
        Otherwise, calculates discount and subtracts from total.
        Ensures final price never goes below 0.0.

        Returns:
            float: Final price after discount.
        """
        # TODO 4b: Calculate final price using self._discount_strategy
        pass
