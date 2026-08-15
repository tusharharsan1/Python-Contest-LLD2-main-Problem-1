"""
TODO 3: Create the DiscountFactory
====================================

This file contains the DiscountFactory class — a dedicated
factory that creates the correct discount strategy based on a
string type.

Your task:
----------
Complete the `DiscountFactory` class below:

Implement the static method `create_discount`:

    @staticmethod
    def create_discount(discount_type: str, **kwargs) -> DiscountStrategy:

This method should:

1. Take a `discount_type` string (e.g. "percentage", "flat") and optional `**kwargs`.

2. Return the correct DiscountStrategy instance:
   - "percentage" → PercentageDiscount(percentage=kwargs["percentage"])
   - "flat"       → FlatDiscount(amount=kwargs["amount"])

3. Raise a ValueError with a helpful message if discount_type is not recognized.

Examples:
---------
  DiscountFactory.create_discount("percentage", percentage=10.0)
    → returns a PercentageDiscount(10.0) object

  DiscountFactory.create_discount("flat", amount=50.0)
    → returns a FlatDiscount(50.0) object

  DiscountFactory.create_discount("mystery")
    → raises ValueError
"""

from strategies.discount_strategy import DiscountStrategy
from strategies.percentage_discount import PercentageDiscount
from strategies.flat_discount import FlatDiscount


class DiscountFactory:
    """Factory to create appropriate DiscountStrategy instances."""

    @staticmethod
    def create_discount(discount_type: str, **kwargs) -> DiscountStrategy:
        # ✏️ TODO 3: Implement factory creation logic based on discount_type
        pass
