"""Tests for the ByteBites backend models."""

import pytest
from models import MenuItem, Menu, Order, Customer


# --- Fixtures ---------------------------------------------------------------

@pytest.fixture
def burger():
    return MenuItem("Spicy Burger", 8.50, "Burgers", 4.7)


@pytest.fixture
def soda():
    return MenuItem("Large Soda", 2.00, "Drinks", 4.1)


@pytest.fixture
def cookie():
    return MenuItem("Choc Chip Cookie", 1.50, "Desserts", 4.9)


# --- MenuItem ---------------------------------------------------------------

def test_menuitem_stores_all_fields(burger):
    assert burger.name == "Spicy Burger"
    assert burger.price == 8.50
    assert burger.category == "Burgers"
    assert burger.popularity_rating == 4.7


# --- Menu -------------------------------------------------------------------

def test_menu_defaults_to_empty():
    assert Menu().items == []


def test_menu_filter_returns_matching_category(burger, soda, cookie):
    menu = Menu([burger, soda, cookie])
    assert menu.filter("Drinks") == [soda]


def test_menu_filter_returns_all_matches(burger, soda):
    another_drink = MenuItem("Coffee", 3.00, "Drinks", 4.5)
    menu = Menu([burger, soda, another_drink])
    assert menu.filter("Drinks") == [soda, another_drink]


def test_menu_filter_no_matches_returns_empty(burger):
    menu = Menu([burger])
    assert menu.filter("Drinks") == []


def test_menu_filter_on_empty_menu():
    assert Menu().filter("Drinks") == []


# --- Order ------------------------------------------------------------------

def test_order_defaults_to_empty():
    assert Order().items == []


def test_order_compute_total_sums_prices(burger, soda):
    order = Order([burger, soda])
    assert order.compute_total() == pytest.approx(10.50)


def test_order_compute_total_single_item(soda):
    assert Order([soda]).compute_total() == pytest.approx(2.00)


def test_order_compute_total_empty_is_zero():
    assert Order().compute_total() == 0


def test_order_compute_total_handles_floats(burger, soda, cookie):
    order = Order([burger, soda, cookie])
    assert order.compute_total() == pytest.approx(12.00)


# --- Customer ---------------------------------------------------------------

def test_customer_defaults_to_empty_history():
    customer = Customer("Alex")
    assert customer.name == "Alex"
    assert customer.purchase_history == []


def test_customer_records_orders(burger, soda):
    customer = Customer("Alex")
    order = Order([burger, soda])
    customer.purchase_history.append(order)
    assert customer.purchase_history == [order]
    assert customer.purchase_history[0].compute_total() == pytest.approx(10.50)


def test_customer_accepts_existing_history(soda):
    order = Order([soda])
    customer = Customer("Sam", [order])
    assert customer.purchase_history == [order]


# --- place_order: the customer <-> order link -------------------------------

def test_new_order_has_no_owner(soda):
    # An order that hasn't been placed yet belongs to nobody.
    assert Order([soda]).customer is None


def test_place_order_records_order_in_history(burger, soda):
    # Placing an order adds it to the customer's purchase history.
    customer = Customer("Alex")
    order = Order([burger, soda])
    customer.place_order(order)
    assert customer.purchase_history == [order]


def test_place_order_sets_the_order_owner(burger):
    # Placing an order tells the order who its customer is.
    customer = Customer("Alex")
    order = Order([burger])
    customer.place_order(order)
    assert order.customer is customer


def test_place_order_accumulates_multiple_orders(burger, soda):
    # A customer can place several orders and all are kept, in order.
    customer = Customer("Alex")
    first = customer.place_order(Order([burger]))
    second = customer.place_order(Order([soda]))
    assert customer.purchase_history == [first, second]
