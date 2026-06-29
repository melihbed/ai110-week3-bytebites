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

    def __repr__(self):
        return f"MenuItem(name={self.name!r}, price={self.price})"


class Menu:
    """The full collection of items, with category filtering."""

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def filter(self, category):
        """Return the items in this menu that match the given category."""
        return [item for item in self.items if item.category == category]


class Order:
    """A single transaction grouping the items a user selected.

    `customer` is a back-reference to the Customer who placed the order. It is
    set by Customer.place_order(); prefer that over assigning it by hand so the
    customer's purchase_history stays in sync.
    """

    def __init__(self, items=None):
        self.items = items if items is not None else []
        self.customer = None

    def compute_total(self):
        """Return the total cost of all items in this order."""
        return sum(item.price for item in self.items)

    def __repr__(self):
        names = [item.name for item in self.items]
        return f"Order(items={names}, total={self.compute_total()})"


class Customer:
    """A customer, tracked by name and past purchase history."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def place_order(self, order):
        """Record an order for this customer, linking both sides together."""
        order.customer = self
        self.purchase_history.append(order)
        return order

    def __repr__(self):
        return f"Customer(name={self.name!r}, orders={len(self.purchase_history)}, LTV={sum(order.compute_total() for order in self.purchase_history)})"

customer_melih = Customer("Melih")

house_burger = MenuItem("House Burger", 18.5, "Food", 4.3)
diet_coke = MenuItem("Diet Coke", 2.00, "Drinks", 4.2)

menu = Menu([house_burger, diet_coke])
order1 = Order([house_burger, diet_coke])
customer_melih.place_order(order1)
print(customer_melih.name)
for order in customer_melih.purchase_history:
    print(order)


print(customer_melih)