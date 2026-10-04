import pytest

from shop import orders


def test_a_pending_order_can_be_paid():
    assert orders.can_transition("pending", "paid")


def test_a_shipped_order_cannot_be_paid_again():
    assert not orders.can_transition("shipped", "paid")


def test_a_pending_order_can_be_cancelled():
    assert orders.cancel_order("pending") == "cancelled"


def test_a_shipped_order_cannot_be_cancelled():
    with pytest.raises(ValueError):
        orders.cancel_order("shipped")


def test_a_delivered_order_cannot_be_cancelled():
    with pytest.raises(ValueError):
        orders.cancel_order("delivered")
