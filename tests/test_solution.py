"""
Unit tests for Maxwell Problem 1 - Discount Engine.
Tests all requirements, boundary conditions, edge cases, and design pattern properties.
"""

import unittest
from abc import ABC

from models.product import Product
from strategies.discount_strategy import DiscountStrategy
from strategies.percentage_discount import PercentageDiscount
from strategies.flat_discount import FlatDiscount
from factory.discount_factory import DiscountFactory
from cart.shopping_cart import ShoppingCart


class TestProduct(unittest.TestCase):
    """Tests for the Product model."""

    def test_valid_product_creation(self):
        p = Product("Book", 299.99)
        self.assertEqual(p.name, "Book")
        self.assertAlmostEqual(p.price, 299.99)

    def test_zero_price_product(self):
        p = Product("Free Sample", 0.0)
        self.assertEqual(p.price, 0.0)

    def test_negative_price_raises_value_error(self):
        with self.assertRaises(ValueError):
            Product("Bad Item", -10.0)


class TestDiscountStrategyInterface(unittest.TestCase):
    """Tests for DiscountStrategy interface and abstract contract."""

    def test_discount_strategy_is_abstract(self):
        self.assertTrue(issubclass(DiscountStrategy, ABC))
        with self.assertRaises(TypeError):
            DiscountStrategy()

    def test_incomplete_subclass_cannot_be_instantiated(self):
        class IncompleteStrategy(DiscountStrategy):
            pass

        with self.assertRaises(TypeError):
            IncompleteStrategy()


class TestPercentageDiscount(unittest.TestCase):
    """Tests for PercentageDiscount strategy."""

    def test_inheritance(self):
        strategy = PercentageDiscount(10.0)
        self.assertIsInstance(strategy, DiscountStrategy)

    def test_standard_percentage_calculation(self):
        strategy = PercentageDiscount(10.0)
        self.assertAlmostEqual(strategy.calculate_discount(500.0), 50.0)

        strategy2 = PercentageDiscount(25.0)
        self.assertAlmostEqual(strategy2.calculate_discount(1000.0), 250.0)

    def test_boundary_zero_percent(self):
        strategy = PercentageDiscount(0.0)
        self.assertAlmostEqual(strategy.calculate_discount(500.0), 0.0)

    def test_boundary_hundred_percent(self):
        strategy = PercentageDiscount(100.0)
        self.assertAlmostEqual(strategy.calculate_discount(500.0), 500.0)

    def test_zero_cart_total(self):
        strategy = PercentageDiscount(20.0)
        self.assertAlmostEqual(strategy.calculate_discount(0.0), 0.0)

    def test_negative_percentage_raises_value_error(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(-1.0)

    def test_percentage_over_hundred_raises_value_error(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(100.1)

    def test_exact_error_message(self):
        try:
            PercentageDiscount(-5.0)
            self.fail("Did not raise ValueError")
        except ValueError as e:
            self.assertIn("Percentage must be between 0 and 100", str(e))


class TestFlatDiscount(unittest.TestCase):
    """Tests for FlatDiscount strategy."""

    def test_inheritance(self):
        strategy = FlatDiscount(50.0)
        self.assertIsInstance(strategy, DiscountStrategy)

    def test_standard_flat_discount_calculation(self):
        strategy = FlatDiscount(100.0)
        self.assertAlmostEqual(strategy.calculate_discount(500.0), 100.0)

    def test_boundary_zero_flat_discount(self):
        strategy = FlatDiscount(0.0)
        self.assertAlmostEqual(strategy.calculate_discount(500.0), 0.0)

    def test_flat_discount_equals_cart_total(self):
        strategy = FlatDiscount(300.0)
        self.assertAlmostEqual(strategy.calculate_discount(300.0), 300.0)

    def test_flat_discount_capped_when_exceeding_cart_total(self):
        strategy = FlatDiscount(500.0)
        # Cart is only 200, discount should be capped at 200, NOT 500
        self.assertAlmostEqual(strategy.calculate_discount(200.0), 200.0)

    def test_flat_discount_on_zero_total_cart(self):
        strategy = FlatDiscount(50.0)
        self.assertAlmostEqual(strategy.calculate_discount(0.0), 0.0)

    def test_negative_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            FlatDiscount(-10.0)

    def test_exact_error_message(self):
        try:
            FlatDiscount(-1.0)
            self.fail("Did not raise ValueError")
        except ValueError as e:
            self.assertIn("Amount cannot be negative", str(e))


class TestDiscountFactory(unittest.TestCase):
    """Tests for DiscountFactory."""

    def test_create_percentage_discount(self):
        strategy = DiscountFactory.create_discount("percentage", percentage=15.0)
        self.assertIsInstance(strategy, PercentageDiscount)
        self.assertAlmostEqual(strategy.calculate_discount(200.0), 30.0)

    def test_create_flat_discount(self):
        strategy = DiscountFactory.create_discount("flat", amount=75.0)
        self.assertIsInstance(strategy, FlatDiscount)
        self.assertAlmostEqual(strategy.calculate_discount(200.0), 75.0)

    def test_case_insensitivity(self):
        s1 = DiscountFactory.create_discount("PERCENTAGE", percentage=10.0)
        self.assertIsInstance(s1, PercentageDiscount)

        s2 = DiscountFactory.create_discount("Flat", amount=20.0)
        self.assertIsInstance(s2, FlatDiscount)

        s3 = DiscountFactory.create_discount("  percentage  ", percentage=5.0)
        self.assertIsInstance(s3, PercentageDiscount)

    def test_unknown_discount_type_raises_value_error(self):
        with self.assertRaises(ValueError) as ctx:
            DiscountFactory.create_discount("coupon")
        self.assertIn("Unknown discount type: coupon", str(ctx.exception))


class TestShoppingCart(unittest.TestCase):
    """Tests for ShoppingCart and strategy integration."""

    def setUp(self):
        self.cart = ShoppingCart()
        self.p1 = Product("Laptop", 1000.0)
        self.p2 = Product("Mouse", 200.0)
        self.p3 = Product("Keyboard", 300.0)

    def test_empty_cart_initial_state(self):
        self.assertEqual(self.cart.get_item_count(), 0)
        self.assertAlmostEqual(self.cart.get_total(), 0.0)
        self.assertAlmostEqual(self.cart.calculate_final_price(), 0.0)

    def test_cart_without_discount_strategy(self):
        self.cart.add_item(self.p1)
        self.cart.add_item(self.p2)
        self.assertAlmostEqual(self.cart.get_total(), 1200.0)
        self.assertAlmostEqual(self.cart.calculate_final_price(), 1200.0)

    def test_cart_with_percentage_discount(self):
        self.cart.add_item(self.p1)
        self.cart.add_item(self.p2)
        self.cart.add_item(self.p3)  # Total = 1500.0

        strategy = PercentageDiscount(10.0)
        self.cart.set_discount_strategy(strategy)

        # 1500 - (10% of 1500) = 1500 - 150 = 1350.0
        self.assertAlmostEqual(self.cart.calculate_final_price(), 1350.0)

    def test_cart_with_flat_discount(self):
        self.cart.add_item(self.p1)
        self.cart.add_item(self.p2)
        self.cart.add_item(self.p3)  # Total = 1500.0

        strategy = FlatDiscount(200.0)
        self.cart.set_discount_strategy(strategy)

        # 1500 - 200 = 1300.0
        self.assertAlmostEqual(self.cart.calculate_final_price(), 1300.0)

    def test_cart_with_excessive_flat_discount_never_goes_below_zero(self):
        self.cart.add_item(self.p2)  # Total = 200.0
        strategy = FlatDiscount(500.0)
        self.cart.set_discount_strategy(strategy)

        self.assertAlmostEqual(self.cart.calculate_final_price(), 0.0)

    def test_strategy_swapping_at_runtime(self):
        self.cart.add_item(self.p1)  # Total = 1000.0

        # Apply 10% discount
        self.cart.set_discount_strategy(PercentageDiscount(10.0))
        self.assertAlmostEqual(self.cart.calculate_final_price(), 900.0)

        # Swap to Flat discount ₹300
        self.cart.set_discount_strategy(FlatDiscount(300.0))
        self.assertAlmostEqual(self.cart.calculate_final_price(), 700.0)

        # Swap to 100% discount
        self.cart.set_discount_strategy(PercentageDiscount(100.0))
        self.assertAlmostEqual(self.cart.calculate_final_price(), 0.0)

    def test_remove_item_updates_final_price(self):
        self.cart.add_item(self.p1)
        self.cart.add_item(self.p2)  # Total = 1200.0
        self.cart.set_discount_strategy(PercentageDiscount(10.0))
        self.assertAlmostEqual(self.cart.calculate_final_price(), 1080.0)

        self.cart.remove_item("Mouse")  # Total becomes 1000.0
        self.assertEqual(self.cart.get_item_count(), 1)
        self.assertAlmostEqual(self.cart.calculate_final_price(), 900.0)

    def test_remove_nonexistent_item_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item("NonExistentItem")

    def test_invalid_strategy_type_raises_error(self):
        with self.assertRaises(TypeError):
            self.cart.set_discount_strategy("not_a_strategy")


class TestEndToEndFactoryAndStrategy(unittest.TestCase):
    """End-to-end integration test combining Factory and Strategy patterns."""

    def test_full_checkout_flow(self):
        cart = ShoppingCart()
        cart.add_item(Product("Headphones", 1500.0))
        cart.add_item(Product("USB Cable", 500.0))

        # 1. Create strategy via Factory
        promo_strategy = DiscountFactory.create_discount("percentage", percentage=20.0)
        cart.set_discount_strategy(promo_strategy)

        # 20% off on 2000.0 = 400.0 discount -> 1600.0
        self.assertAlmostEqual(cart.calculate_final_price(), 1600.0)


if __name__ == "__main__":
    unittest.main()
