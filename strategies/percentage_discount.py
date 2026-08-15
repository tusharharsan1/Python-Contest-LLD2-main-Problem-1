from strategies.discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    """Applies a percentage discount to the cart total."""

    def __init__(self, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100")
        self.percentage = float(percentage)

    def calculate_discount(self, cart_total: float) -> float:
        return (self.percentage / 100.0) * float(cart_total)
