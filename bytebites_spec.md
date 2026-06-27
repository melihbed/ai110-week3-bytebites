Add a heading "Candidate Classes" and list the four nouns you believe the system must model. Use your own judgment here; the goal is to identify the core data objects the system needs.

## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes

### Customer

- name: String
- purchaseHistory: Order[]

### MenuItem

- name: String
- price: float
- category: String
- popularityRating: float

### Menu

- items: MenuItem[]
- filter(category: String): MenuItem[]

### Order

- items: MenuItem[]
- computeTotal(): float

## Class Diagram

```mermaid
classDiagram
    class Customer {
        +String name
        +Order[] purchaseHistory
    }

    class MenuItem {
        +String name
        +float price
        +String category
        +float popularityRating
    }

    class Menu {
        +MenuItem[] items
        +filter(category: String) MenuItem[]
    }

    class Order {
        +MenuItem[] items
        +computeTotal() float
    }

    Customer "1" o-- "*" Order : purchaseHistory
    Order "1" o-- "*" MenuItem : items
    Menu "1" o-- "*" MenuItem : items
```
