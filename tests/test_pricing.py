import pytest

from shop import pricing


def test_discount_takes_the_percentage_off():
    assert pricing.apply_discount(200.0, 10) == 180.0


def test_discount_rejects_more_than_100_percent():
    with pytest.raises(ValueError):
        pricing.apply_discount(50.0, 120)


def test_bulk_discount_starts_at_ten_units():
    assert pricing.bulk_unit_price(20.0, 10) == 17.0


def test_no_bulk_discount_below_ten_units():
    assert pricing.bulk_unit_price(20.0, 9) == 20.0


def test_cart_total_adds_tax():
    assert pricing.cart_total([10.0, 10.0], 0.1) == 22.0


def test_empty_cart_costs_nothing():
    assert pricing.cart_total([]) == 0.0
