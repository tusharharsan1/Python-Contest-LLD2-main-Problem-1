# Maxwell Problem 1 - Discount Engine

## Problem statement

You are building the discount engine for an e-commerce platform called ShopSmart.
When a customer adds products to their cart and proceeds to checkout, the system
must calculate and apply the appropriate discount to determine their final price.

Different promotions offer different ways of calculating discounts (such as a
percentage off the total, or a flat rupee amount deduction). Because these
discount algorithms can vary and new discount types may be added over time, you
will model each discount as a separate strategy following the **Strategy Pattern**.

To keep the rest of the application decoupled from the concrete strategy classes,
you will also build a `DiscountFactory` following the **Factory Pattern** that
centralizes the instantiation of discount objects based on a type name.

Finally, the `ShoppingCart` class manages products and uses the assigned discount
strategy to compute the final price at checkout.

You are given two pre-written building blocks: `models/product.py` (which represents
a product) and `strategies/discount_strategy.py` (which defines the abstract base
interface). Do not edit these files.

## Requirements

### Product and Strategy Base (Pre-written)

- `Product(name, price)` stores `name` and `price`. `price` cannot be negative.
- `DiscountStrategy` is an abstract base class with one abstract method:
  `calculate_discount(cart_total)`.

### Strategies

Each discount strategy inherits from `DiscountStrategy` and implements
`calculate_discount(cart_total)` returning a `float`:

- `PercentageDiscount(percentage)`:
  - Takes a `percentage` (`float`).
  - Validates `0 <= percentage <= 100`. If out of range, raise `ValueError("Percentage must be between 0 and 100")`.
  - `calculate_discount(cart_total)` returns `(percentage / 100.0) * cart_total`.

- `FlatDiscount(amount)`:
  - Takes an `amount` (`float`).
  - Validates `amount >= 0`. If negative, raise `ValueError("Amount cannot be negative")`.
  - `calculate_discount(cart_total)` returns the discount amount.
  - The discount amount must never exceed `cart_total` (capped at `cart_total`).

### Discount Factory

- `DiscountFactory.create_discount(discount_type, **kwargs)` is a static method:
  - When `discount_type.lower() == "percentage"`, returns a `PercentageDiscount(percentage=kwargs["percentage"])`.
  - When `discount_type.lower() == "flat"`, returns a `FlatDiscount(amount=kwargs["amount"])`.
  - If `discount_type` is anything else, raise `ValueError(f"Unknown discount type: {discount_type}")`.

### Shopping Cart

- `ShoppingCart()` starts with an empty item list and no discount strategy (`None`).
- `add_item(product)` adds a product to the cart (pre-written).
- `remove_item(product_name)` removes the first product matching `product_name` (pre-written).
- `get_total()` returns the sum of all item prices in the cart as a `float` (pre-written).
- `get_item_count()` returns the number of items in the cart (pre-written).
- `set_discount_strategy(strategy)` sets `self._discount_strategy` to the given `DiscountStrategy` object.
- `calculate_final_price()` calculates and returns the final price after discount as a `float`:
  - If no discount strategy is set (`None`), returns `get_total()`.
  - If a strategy is set, computes `discount = strategy.calculate_discount(self.get_total())` and subtracts it from `get_total()`.
  - The final price must never go below `0.0` (use `max(0.0, ...)`).

## Instructions

1. `models/product.py` and `strategies/discount_strategy.py` are already completed. Do not edit these files.
2. Implement the TODOs in `strategies/percentage_discount.py`, `strategies/flat_discount.py`, `factory/discount_factory.py`, and `cart/shopping_cart.py`.
3. Keep class names, method names, and signatures exactly as given.
4. Follow the TODO comments in the starter files.
5. Use the exact error message specified in the requirements.
6. Use only the Python standard library.
