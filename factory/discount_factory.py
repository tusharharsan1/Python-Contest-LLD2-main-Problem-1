from strategies.discount_strategy import DiscountStrategy
from strategies.percentage_discount import PercentageDiscount
from strategies.flat_discount import FlatDiscount


class DiscountFactory:
    """Factory to create appropriate DiscountStrategy instances."""

    @staticmethod
    def create_discount(discount_type: str, **kwargs) -> DiscountStrategy:
        dtype = str(discount_type).strip().lower()
        if dtype == "percentage":
            if "percentage" not in kwargs:
                raise ValueError("Missing 'percentage' argument for PercentageDiscount")
            return PercentageDiscount(percentage=kwargs["percentage"])
        elif dtype == "flat":
            if "amount" not in kwargs:
                raise ValueError("Missing 'amount' argument for FlatDiscount")
            return FlatDiscount(amount=kwargs["amount"])
        else:
            raise ValueError(f"Unknown discount type: {discount_type}")
