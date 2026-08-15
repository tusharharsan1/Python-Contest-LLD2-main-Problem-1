from strategies.discount_strategy import DiscountStrategy


class FlatDiscount(DiscountStrategy):
    """Applies a flat amount discount capped at the cart total."""

    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = float(amount)

    def calculate_discount(self, cart_total: float) -> float:
        return min(self.amount, float(cart_total))
