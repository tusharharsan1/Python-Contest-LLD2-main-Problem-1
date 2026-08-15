"""
PRE-WRITTEN INTERFACE — DO NOT MODIFY THIS FILE
================================================

This file contains the DiscountStrategy abstract base class (the interface).
Read it to understand the contract that all discount strategies must follow.
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Abstract base class (interface) for all discount strategies.

    Every concrete discount strategy must implement the calculate_discount method.
    """

    @abstractmethod
    def calculate_discount(self, cart_total: float) -> float:
        """Calculate and return the discount amount for a given cart total.

        Args:
            cart_total (float): Total price of items in the cart.

        Returns:
            float: The discount amount to subtract from the cart total.
        """
        pass
