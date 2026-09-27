"""Input checks."""

import re

_SKU = re.compile(r"^[A-Z]{3}-\d{4}$")
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_sku(sku: str) -> bool:
    """SKUs look like ABC-1234.

    >>> is_valid_sku("ABC-1234")
    True
    >>> is_valid_sku("abc-12")
    False
    """
    return bool(_SKU.match(sku))


def is_valid_email(email: str) -> bool:
    """A pragmatic check: something@domain.tld.

    >>> is_valid_email("sam@example.com")
    True
    >>> is_valid_email("sam@")
    False
    """
    return bool(_EMAIL.match(email))
