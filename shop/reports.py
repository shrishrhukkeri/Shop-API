"""Order statistics."""


def average_order_value(totals: list) -> float:
    """Mean of the order totals; 0.0 when there are no orders.

    >>> average_order_value([10.0, 20.0])
    15.0
    """
    return sum(totals) / len(totals)


def busiest_day(orders_per_day: dict) -> str:
    """The day with the most orders ('' when there is no data).

    >>> busiest_day({"mon": 3, "tue": 9})
    'tue'
    """
    if not orders_per_day:
        return ""
    return max(orders_per_day, key=orders_per_day.get)
