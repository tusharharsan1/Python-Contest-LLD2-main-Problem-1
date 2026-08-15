from typing import Optional
from models.product import Product
from strategies.discount_strategy import DiscountStrategy


class ShoppingCart:
    """A shopping cart that holds products and applies a discount strategy to calculate the final price."""

    def __init__(self):
        self._items = []
        self._discount_strategy: Optional[DiscountStrategy] = None

    def add_item(self, product: Product):
        """Add a product to the cart."""
        self._items.append(product)

    def remove_item(self, product_name: str):
        """Remove the first product with the given name from the cart."""
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

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Set or swap the discount strategy for this shopping cart."""
        if not isinstance(strategy, DiscountStrategy):
            raise TypeError("strategy must be an instance of DiscountStrategy")
        self._discount_strategy = strategy

    def calculate_final_price(self) -> float:
        """Calculate the final price of the cart after applying discount strategy."""
        total = self.get_total()
        if self._discount_strategy is None:
            return float(total)

        discount = self._discount_strategy.calculate_discount(total)
        final_price = total - discount
        return float(max(0.0, final_price))
