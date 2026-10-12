"""Shipping cost by parcel weight."""

EXPRESS_SURCHARGE = 7.50


def shipping_cost(weight_kg: float, express: bool = False) -> float:
    """Flat tiers: up to 1 kg costs 4.99, up to 5 kg costs 8.99, anything heavier 14.99.
    Express delivery adds 7.50.

    >>> shipping_cost(1.0)
    4.99
    >>> shipping_cost(5.0)
    8.99
    >>> shipping_cost(2.5, express=True)
    16.49
    """
    if weight_kg <= 1:
        cost = 4.99
    elif weight_kg <= 5:
        cost = 8.99
    else:
        cost = 14.99
    if express:
        cost += EXPRESS_SURCHARGE
    return round(cost, 2)
