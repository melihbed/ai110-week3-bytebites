"""
ByteBites backend models.

Four core classes for the campus food-ordering app: MenuItem, Menu, Order, and Customer. Plain Python classes only — no persistence, auth, or DB layer.
"""


class MenuItem:
    """A single sellable item, e.g. a "Spicy Burger" or "Large Soda"."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of items, with category filtering."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter(self, category):
        """Return the items in this menu that match the given category."""
        return [item for item in self.items if item.category == category]


class Order:
    """A single transaction grouping the items a user selected."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def compute_total(self):
        """Return the total cost of all items in this order."""
        return sum(item.price for item in self.items)


class Customer:
    """A customer, tracked by name and past purchase history."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []
