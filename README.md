# Shop API

Business rules for a small online shop: pricing, stock, orders, shipping and loyalty points.
Plain Python, no framework, so every rule can be tested on its own.

```
shop/pricing.py     discounts, bulk prices, cart totals
shop/inventory.py   stock levels and reservations
shop/orders.py      the order life cycle
shop/shipping.py    shipping cost by weight
shop/loyalty.py     loyalty points
shop/reports.py     order statistics
shop/validators.py  input checks
```

Run the tests with `pytest`.
