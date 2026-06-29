"""Quick demo — create a few ByteBites objects and print their attributes.

Run with: python3 demo.py
"""

from models import MenuItem, Menu, Order, Customer

print("=== MenuItem ===")
burger = MenuItem("Spicy Burger", 8.50, "Burgers", 4.7)
soda = MenuItem("Large Soda", 2.00, "Drinks", 4.1)
cookie = MenuItem("Choc Chip Cookie", 1.50, "Desserts", 4.9)
for item in (burger, soda, cookie):
    print(vars(item))

print("\n=== Menu ===")
menu = Menu([burger, soda, cookie])
print("item names:", [i.name for i in menu.items])
print("filter('Drinks'):", [i.name for i in menu.filter("Drinks")])
print("empty Menu().items:", Menu().items)

print("\n=== Order ===")
order = Order([burger, soda])
print("order items:", [i.name for i in order.items])
print("compute_total():", order.compute_total())
print("empty Order().compute_total():", Order().compute_total())

print("\n=== Customer ===")
alex = Customer("Alex")
print("new customer:", alex.name, "| history:", alex.purchase_history)
alex.purchase_history.append(order)
print("after one order -> history length:", len(alex.purchase_history))
print("first order total:", alex.purchase_history[0].compute_total())

print("\nAll objects created and inspected without errors.")
