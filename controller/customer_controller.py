from model.customer import Customer


def create_customer(
    customer_id,
    first_name,
    last_name,
    phone_number,
    address,
    gender
):
    customer = Customer(
        customer_id=int(customer_id),
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
        gender=gender
    )

    customer.save_customer()

    return customer

def get_customer(customer_id):
    return Customer.load_customer(int(customer_id))

def get_all_customers():
    return Customer.load_all_customers()

def search_customers(query):
    query = str(query).strip()

    customers = Customer.load_all_customers()

    if not query:
        return list(customers.values())

    results = []

    for customer in customers.values():
        if (
            query == str(customer.customer_id)
            or query in customer.phone_number
        ):
            results.append(customer)

    return results

def update_customer_info(
    customer_id,
    first_name,
    last_name,
    phone_number,
    address,
    gender
):
    updated_customer = Customer(
        customer_id=int(customer_id),
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
        gender=gender
    )

    updated_customer.update_customer()
    return updated_customer

import pickle
from pathlib import Path


def check_customer_deletion(customer_id):
    customer_id = int(customer_id)

    customer = Customer.load_customer(customer_id)

    orders_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "orders.pkl"
    )

    if not orders_file.is_file():
        raise FileNotFoundError(
            "فایل سفارش‌ها پیدا نشد؛ حذف مشتری مجاز نیست."
        )

    with orders_file.open("rb") as file:
        orders = pickle.load(file)

    if not isinstance(orders, dict):
        raise ValueError("ساختار فایل سفارش‌ها معتبر نیست.")

    for order in orders.values():
        if order.customer.customer_id == customer_id:
            return customer, False

    return customer, True

def delete_customer(customer_id):
    customer, can_delete = check_customer_deletion(customer_id)

    if not can_delete:
        raise ValueError(
            "این مشتری سفارش ثبت‌شده دارد و قابل حذف نیست."
        )

    Customer.delete_customer(int(customer_id))