"""
TODO 1: Create the PercentageDiscount strategy
===============================================

This file contains the PercentageDiscount class — a concrete
strategy that applies a percentage-based discount to the cart total.

Your task:
----------
Complete the `PercentageDiscount` class below:

1. Implement `__init__(self, percentage: float)`:
   - Example: 10.0 means "10% off"
   - Validate that percentage is between 0 and 100 (inclusive): 0 <= percentage <= 100
   - Raise a ValueError with a message if it is out of range.
   - Store percentage in an instance variable `self.percentage`.

2. Implement `calculate_discount(self, cart_total: float) -> float`:
   - Returns: (self.percentage / 100.0) * cart_total

Examples:
---------
  strategy = PercentageDiscount(10.0)
  strategy.calculate_discount(500.0)   → 50.0
  strategy.calculate_discount(1000.0)  → 100.0
  strategy.calculate_discount(0.0)     → 0.0

  PercentageDiscount(-5.0)   → raises ValueError
  PercentageDiscount(150.0)  → raises ValueError
"""

from strategies.discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    """Applies a percentage discount to the cart total."""

    def __init__(self, percentage: float):
        # ✏️ TODO 1a: Validate percentage (0 <= percentage <= 100) and store it
        pass

    def calculate_discount(self, cart_total: float) -> float:
        # ✏️ TODO 1b: Calculate and return the percentage discount
        pass
