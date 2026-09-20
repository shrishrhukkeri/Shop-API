"""The order life cycle."""

TRANSITIONS = {
    "pending": {"paid", "cancelled"},
    "paid": {"shipped", "refunded"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
    "refunded": set(),
}


def can_transition(current: str, new: str) -> bool:
    """True when an order may move from `current` to `new`.

    >>> can_transition("pending", "paid")
    True
    >>> can_transition("shipped", "paid")
    False
    """
    return new in TRANSITIONS.get(current, set())


def cancel_order(status: str) -> str:
    """Cancel an order that has not shipped yet.

    >>> cancel_order("pending")
    'cancelled'
    """
    if status in ("delivered", "refunded", "cancelled"):
        raise ValueError(f"an order that is {status} cannot be cancelled")
    return "cancelled"
