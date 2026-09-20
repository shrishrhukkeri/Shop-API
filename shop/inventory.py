"""Stock levels and reservations."""


class Inventory:
    """Tracks how many units of each SKU are on the shelf."""

    def __init__(self, stock=None):
        self._stock = dict(stock or {})

    def available(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def restock(self, sku: str, quantity: int) -> int:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._stock[sku] = self.available(sku) + quantity
        return self._stock[sku]

    def reserve(self, sku: str, quantity: int) -> bool:
        """Take `quantity` units off the shelf. False when there is not enough stock."""
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.available(sku) <= quantity:
            return False
        self._stock[sku] -= quantity
        return True
