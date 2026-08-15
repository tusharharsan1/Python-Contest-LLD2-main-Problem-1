"""
TODO 2: Create the FlatDiscount strategy
=========================================

This file contains the FlatDiscount class — a concrete
strategy that subtracts a fixed amount from the cart total.

Your task:
----------
Complete the `FlatDiscount` class below:

1. Implement `__init__(self, amount: float)`:
   - This is the fixed discount amount (e.g., 100.0 means "₹100 off")
   - Validate that amount is not negative (amount >= 0).
     Raise a ValueError with a message if it is negative.
   - Store amount in an instance variable `self.amount`.

2. Implement `calculate_discount(self, cart_total: float) -> float`:
   - Returns the flat discount amount.
   - IMPORTANT: The discount must NEVER exceed the cart_total.
     If the flat amount is greater than the cart total,
     return the cart_total instead (cap it using min(self.amount, cart_total)).

Examples:
---------
  strategy = FlatDiscount(100.0)
  strategy.calculate_discount(500.0)  → 100.0
  strategy.calculate_discount(80.0)   → 80.0   (capped at cart_total)
  strategy.calculate_discount(100.0)  → 100.0
  strategy.calculate_discount(0.0)    → 0.0

  FlatDiscount(-50.0)  → raises ValueError
"""

from strategies.discount_strategy import DiscountStrategy


class FlatDiscount(DiscountStrategy):
    """Applies a flat amount discount capped at the cart total."""

    def __init__(self, amount: float):
        # ✏️ TODO 2a: Validate amount (amount >= 0) and store it
        pass

    def calculate_discount(self, cart_total: float) -> float:
        # ✏️ TODO 2b: Return discount capped at cart_total
        pass
