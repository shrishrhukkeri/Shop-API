"""Loyalty points."""

TIER_MULTIPLIER = {"basic": 1, "silver": 1.5, "gold": 2}


def points_for_order(total: float, tier: str = "basic") -> int:
    """One point per whole currency unit, multiplied by the customer's tier.

    >>> points_for_order(100.0)
    100
    >>> points_for_order(100.0, "gold")
    200
    """
    multiplier = TIER_MULTIPLIER.get(tier, 1)
    bonus = 0
    if tier == "platinum":
        bonus = platinum_bonus(total)
    return int(total * multiplier) + bonus


def points_value(points: int) -> int:
    """What `points` are worth at checkout, in whole cents (two points per cent)."""
    return points / 2
