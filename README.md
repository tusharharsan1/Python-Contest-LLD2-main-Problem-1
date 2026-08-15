# Maxwell Problem 1: ShopSmart Discount Engine

## Time Limit: 35 minutes

---

## Problem Description

You are building the **discount engine** for an online store called **ShopSmart**.

When a customer adds products to their shopping cart and checks out, the store applies a **discount** to their order based on the current promotion.

ShopSmart supports **two types of discounts**:

| Discount Type | How It Works |
|---|---|
| **Percentage Discount** | Takes a percentage off the cart total. Example: 10% off a ₹500 cart = ₹50 discount (Final price: ₹450). |
| **Flat Discount** | Subtracts a fixed amount from the cart total. Example: ₹100 off a ₹500 cart = ₹100 discount (Final price: ₹400). The discount can never exceed the cart total. |

---

## Project Structure

```
Maxwell Problem 1/
├── README.md                           ← Problem description & instructions
│
├── models/
│   ├── __init__.py
│   └── product.py                      ✅ Pre-written Product class (DO NOT MODIFY)
│
├── strategies/
│   ├── __init__.py
│   ├── discount_strategy.py            ✅ Pre-written interface (DO NOT MODIFY)
│   ├── percentage_discount.py          📝 TODO 1 — PercentageDiscount class
│   └── flat_discount.py                📝 TODO 2 — FlatDiscount class
│
├── factory/
│   ├── __init__.py
│   └── discount_factory.py             📝 TODO 3 — DiscountFactory class
│
└── cart/
    ├── __init__.py
    └── shopping_cart.py                📝 TODO 4a, 4b — ShoppingCart discount methods
```

---

## What You Need To Build

Open each file listed below and implement the code where the `✏️ TODO` comment is marked:

| TODO | File to Edit | Task Description |
|---|---|---|
| **1** | `strategies/percentage_discount.py` | Implement `__init__` (validate 0–100%) and `calculate_discount` |
| **2** | `strategies/flat_discount.py` | Implement `__init__` (validate >= 0) and `calculate_discount` (cap at total) |
| **3** | `factory/discount_factory.py` | Implement `create_discount(discount_type, **kwargs)` factory method |
| **4a, 4b** | `cart/shopping_cart.py` | Implement `set_discount_strategy` and `calculate_final_price` |

---

## Example Walkthrough

```
Cart items: [Laptop(₹1000), Mouse(₹200), Keyboard(₹300)]
Cart Total: ₹1500

1. With PercentageDiscount(10.0):
   Discount = 10% of 1500 = ₹150
   Final Price = 1500 - 150 = ₹1350

2. With FlatDiscount(200.0):
   Discount = ₹200
   Final Price = 1500 - 200 = ₹1300

3. With FlatDiscount(2000.0) [exceeds cart total]:
   Discount = capped at ₹1500
   Final Price = max(0, 1500 - 1500) = ₹0
```

---

## Important Rules

- Use **only** standard Python (no third-party packages).
- Do **NOT** modify any file marked with `DO NOT MODIFY`.
- All discount amounts and final prices must be returned as `float`.
- Final price after discount must **never go below 0.0**.

Good luck!
