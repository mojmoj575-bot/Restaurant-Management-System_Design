import pickle
from pathlib import Path


def load_orders():
    orders_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "orders.pkl"
    )

    if not orders_file.exists():
        return {}

    with orders_file.open("rb") as file:
        orders = pickle.load(file)

    if not isinstance(orders, dict):
        raise ValueError("ساختار فایل سفارش‌ها معتبر نیست.")

    return orders

def search_orders(orders, query):
    query = str(query).strip().lower().replace("ي", "ی")

    if not query:
        return list(orders.values())

    results = []

    for order in orders.values():
        customer = order.customer

        customer_name = (
            f"{customer.first_name} "
            f"{customer.last_name}"
        )

        order_id_text = str(order.order_id)

        if (
            query in order_id_text
            or query in customer_name.lower().replace("ي", "ی")
        ):
            results.append(order)

    return results

from model.order import Order
from model.customer import Customer


def create_order(customer, menu):
    if not isinstance(customer, Customer):
        raise ValueError("ابتدا اطلاعات مشتری را ثبت یا انتخاب کنید.")

    order_id = Order.get_next_order_id()

    return Order(
        order_id=order_id,
        customer=customer,
        menu=menu
    )


def add_item_to_order(order, food_name, quantity):
    if order is None:
        raise ValueError("سفارشی برای افزودن غذا وجود ندارد.")

    food_name = food_name.strip()
    quantity = int(quantity)

    if not food_name:
        raise ValueError("ابتدا یک غذا انتخاب کنید.")

    if quantity <= 0:
        raise ValueError("تعداد غذا باید بیشتر از صفر باشد.")

    order.add_item(food_name, quantity)

    return order

def finalize_order(order):
    if not isinstance(order, Order):
        raise ValueError("سفارش معتبری وجود ندارد.")

    if not order.get_items():
        raise ValueError("سفارش خالی قابل ثبت نیست.")

    order.save_order()

    return order.order_id

def remove_item_from_order(order, food_name):
    if not isinstance(order, Order):
        raise ValueError("سفارش معتبری وجود ندارد.")

    order.remove_item(food_name)
    return order