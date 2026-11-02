from model.menu import Menu


def get_menu():
    try:
        return Menu.load_menu()
    except FileNotFoundError:
        return Menu()

def add_food(menu, food_name, price):
    food_name = food_name.strip()

    if not food_name:
        raise ValueError("نام غذا نمی‌تواند خالی باشد.")

    price = int(price)

    if price <= 0:
        raise ValueError("قیمت باید بیشتر از صفر باشد.")

    if food_name in menu.get_items():
        raise ValueError("این غذا قبلاً در منو وجود دارد.")

    menu.add_item(food_name, price)
    menu.save_menu()

    return menu

def update_food_price(menu, food_name, new_price):
    new_price = int(new_price)

    if new_price <= 0:
        raise ValueError("قیمت باید بیشتر از صفر باشد.")

    items = menu.get_items()

    if food_name not in items:
        raise ValueError("غذای انتخاب‌شده در منو وجود ندارد.")

    old_price = items[food_name]

    menu.update_price(food_name, new_price)

    try:
        menu.save_menu()
    except OSError:
        menu.update_price(food_name, old_price)
        raise

    return menu

def delete_food(menu, food_name):
    old_items = menu.get_items().copy()

    if food_name not in old_items:
        raise ValueError("غذای انتخاب‌شده در منو وجود ندارد.")

    menu.remove_item(food_name)

    try:
        menu.save_menu()
    except OSError:
        menu._items = old_items
        raise

    return menu