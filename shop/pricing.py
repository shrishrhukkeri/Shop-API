"""Pricing rules: discounts, bulk prices and cart totals."""

TAX_RATE = 0.08
BULK_THRESHOLD = 10
BULK_DISCOUNT_PERCENT = 15


def apply_discount(price: float, percent: float) -> float:
    """Return `price` after taking `percent` off.

    >>> apply_discount(100.0, 10)
    90.0
    >>> apply_discount(80.0, 25)
    60.0
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price - price * percent / 100, 2)


def bulk_unit_price(unit_price: float, quantity: int) -> float:
    """Orders of 10 or more units get 15% off the unit price.

    >>> bulk_unit_price(20.0, 10)
    17.0
    >>> bulk_unit_price(20.0, 9)
    20.0
    """
    if quantity > BULK_THRESHOLD:
        return apply_discount(unit_price, BULK_DISCOUNT_PERCENT)
    return unit_price


def cart_total(prices: list, tax_rate: float = TAX_RATE) -> float:
    """Total of a cart including tax.

    >>> cart_total([10.0, 5.0], 0.1)
    16.5
    """
    subtotal = sum(prices)
    return round(subtotal * (1 + tax_rate), 2)
