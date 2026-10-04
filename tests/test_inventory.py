import pytest

from shop.inventory import Inventory


def test_reserve_reduces_stock():
    inv = Inventory({"ABC-1000": 10})
    assert inv.reserve("ABC-1000", 4) is True
    assert inv.available("ABC-1000") == 6


def test_cannot_reserve_more_than_is_in_stock():
    inv = Inventory({"ABC-1000": 3})
    assert inv.reserve("ABC-1000", 5) is False
    assert inv.available("ABC-1000") == 3


def test_the_last_units_can_be_reserved():
    inv = Inventory({"ABC-1000": 3})
    assert inv.reserve("ABC-1000", 3) is True
    assert inv.available("ABC-1000") == 0


def test_restock_adds_units():
    inv = Inventory()
    assert inv.restock("ABC-1000", 5) == 5


def test_zero_quantity_is_rejected():
    with pytest.raises(ValueError):
        Inventory({"ABC-1000": 1}).reserve("ABC-1000", 0)
