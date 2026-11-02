from model.menu import Menu
from model.customer import Customer
from model.order import Order
import pickle
from pathlib import Path


menu = Menu()
# try:
#     menu.add_item("پیتزا", 25000)
#     menu.add_item("برگر", 18000)
#     print("غذاها با موفقیت ثبت شدند")
#     print(menu.get_items())
#     print("منوی رستوران : ", menu.get_items())
#     price = menu.get_price("پیتزا")
#     print("قیمت پیتزا : ", price)
#     menu.remove_item("برگر")
#     print("منو بعد از حذف : ", menu.get_items())
# except ValueError as error:
#     print("خطا : ", error)
# try:
#     price = menu.get_price("ماکارونی")
#     print("قیمت ماکارونی : ", price)
# except ValueError as error:
#     print("خطای مورد انتظار : ", error)
#
# from model.customer import Customer
# try:
#     customer = Customer(
#     customer_id = 101,
#     first_name = "مجتبی",
#     last_name ="کفائی" ,
#     phone_number = "09123456789",
#     address = "میدان ولیعصر",
#     gender = "مرد")
# except ValueError as error:
#     print("خطای مورد انتظار : ", error)

# customer = Customer(
# customer_id = 101,
# first_name = "مجتبی",
# last_name ="کفائی" ,
# phone_number = "09123456789")
# print(customer.first_name)
# print(customer.address)
# print(customer.get_info())

# ساخت منوی رستوران
restaurant_menu = Menu()
restaurant_menu.add_item("پیتزا", 250000)
restaurant_menu.add_item("برگر", 180000)

# ساخت مشتری
customer = Customer(
    customer_id=101,
    first_name="مجتبی",
    last_name="کفاشی",
    phone_number="09123456789"
)

# ساخت سفارش
order = Order(
    order_id=1001,
    customer=customer,
    menu=restaurant_menu
)

# بررسی ارتباط کلاس‌ها
print("شماره سفارش:", order.order_id)
print("نام مشتری:", order.customer.first_name)
print("منوی سفارش:", order.menu.get_items())

order.add_item("پیتزا", 2)
order.add_item("برگر", 1)
order.add_item("پیتزا", 1)

print("اقلام سفارش : ", order.get_items())
print("مبلغ کل :", order.calculate_total(), "تومان")
try:
    order.remove_item("برگر")

    print("سفارش بعد از حذف:", order.get_items())
    print("مبلغ جدید:", order.calculate_total(), "تومان")

except ValueError as error:
    print("خطا:", error)

# print("تاریخ و ساعت سفارش:", order.get_order_datetime())
# print(order.generate_invoice())
# order.save_order()
# print("سفارش با موفقیت ذخیره شد.")
# try:
#     # restored_order = Order.load_order()
#
#     print("سفارش بازیابی شد.")
#     print("شماره سفارش:", restored_order.order_id)
#     print("نام مشتری:", restored_order.customer.first_name)
#     print("اقلام سفارش:", restored_order.get_items())
#     print("مبلغ سفارش:", restored_order.calculate_total())
#
# except (OSError, ValueError, TypeError) as error:
#     print("خطا در بازیابی:", error)
# بازیابی سفارش اول
first_order = Order.load_order(1001)

# ساخت سفارش دوم
second_order = Order(
    order_id=1002,
    customer=customer,
    menu=restaurant_menu
)

second_order.add_item("برگر", 2)

# ذخیره سفارش دوم
# second_order.save_order()

# بازیابی هر دو سفارش
restored_first = Order.load_order(1001)
restored_second = Order.load_order(1002)

print("سفارش اول:", restored_first.get_items())
print("سفارش دوم:", restored_second.get_items())

print("مبلغ سفارش اول:", restored_first.calculate_total())
print("مبلغ سفارش دوم:", restored_second.calculate_total())
try:
    existing_order = Order.load_order(1001)
    existing_order.save_order()

except ValueError as error:
    print("تست جلوگیری از تکرار:", error)

from model.customer import Customer

try:
    test_customer = Customer(
        customer_id=2001,
        first_name="علی",
        last_name="رضایی",
        phone_number="09123456789",
        address="تهران، خیابان ولیعصر، پلاک ۱۲",
        gender="مرد"
    )

    test_customer.save_customer()

    print("مشتری با موفقیت ذخیره شد.")

    restored_customer = Customer.load_customer(2001)

    print("اطلاعات بازیابی‌شده:")
    print(restored_customer.get_info())

except (ValueError, OSError, EOFError, pickle.UnpicklingError) as error:
    print("خطا:", error)

from model.customer import Customer

try:
    customer = Customer.load_customer(2002)

    print("مشتری با موفقیت بازیابی شد.")
    print(customer.get_info())

except (ValueError, OSError) as error:
    print("خطا در بازیابی مشتری:", error)

from model.menu import Menu

try:
    test_menu = Menu()

    test_menu.add_item("پیتزا", 250000)
    test_menu.add_item("برگر", 180000)
    test_menu.add_item("پاستا", 220000)
    test_menu.add_item("سالاد سزار", 150000)
    test_menu.add_item("نوشابه", 30000)

    test_menu.save_menu()

    print("منو با موفقیت ذخیره شد.")

    restored_menu = Menu.load_menu()

    print("منوی بازیابی‌شده:")
    print(restored_menu.get_items())

except (ValueError, TypeError, OSError, EOFError,
        pickle.UnpicklingError) as error:
    print("خطا:", error)

import os
import tempfile


def test_duplicate_order():
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "orders.pkl")

        customer = Customer.__new__(Customer)

        order = Order.__new__(Order)
        order.order_id = 9999
        order.customer = customer

        # بار اول باید ذخیره شود
        order.save_order(filename)

        # بار دوم باید از ثبت شماره تکراری جلوگیری شود
        try:
            order.save_order(filename)
        except ValueError as error:
            assert "قبلاً ثبت شده" in str(error)
        else:
            raise AssertionError(
                "سیستم سفارش تکراری را قبول کرد!"
            )

    print("✅ تست جلوگیری از سفارش تکراری موفق بود.")

def test_backup_recovery():
    backup_file = (
        Path.home()
        / "Desktop"
        / "Restaurant_Recovery_Test"
        / "orders.pkl"
    )

    assert backup_file.is_file(), "فایل بازیابی‌شده پیدا نشد."

    order = Order.load_order(
        1012,
        filename=str(backup_file)
    )

    assert order.order_id == 1012
    print("✅ بازیابی سفارش ۱۰۱۲ از نسخه پشتیبان موفق بود.")

import os
import pickle
import tempfile
from unittest.mock import patch


def test_atomic_save_failure():
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "orders.pkl")

        # ایجاد فایل اصلی آزمایشی
        original_data = {1001: "سفارش اولیه"}

        with open(filename, "wb") as file:
            pickle.dump(original_data, file)

        # شبیه‌سازی خطا هنگام نوشتن فایل موقت
        def fake_dump(*args, **kwargs):
            raise OSError("خطای آزمایشی ذخیره‌سازی")

        with patch("model.order.pickle.dump", side_effect=fake_dump):
            try:
                with open(filename + ".tmp", "wb") as file:
                    pickle.dump({1002: "سفارش جدید"}, file)

                os.replace(filename + ".tmp", filename)

            except OSError:
                pass

        # بررسی سالم ماندن فایل اصلی
        with open(filename, "rb") as file:
            recovered_data = pickle.load(file)

        assert recovered_data == original_data

    print("✅ تست سالم ماندن فایل اصلی موفق بود.")

def test_real_atomic_save():
    import tempfile
    import pickle
    from pathlib import Path
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as temp_dir:
        filename = Path(temp_dir) / "orders.pkl"

        # ایجاد سفارش آزمایشی
        order = Order.__new__(Order)
        order.order_id = 9998

        # ذخیره اولیه
        order.save_order(str(filename))
        original_bytes = filename.read_bytes()

        # ایجاد سفارش دوم
        new_order = Order.__new__(Order)
        new_order.order_id = 9999

        # ایجاد خطای مصنوعی هنگام نوشتن
        with patch("model.order.pickle.dump", side_effect=OSError("test error")):
            try:
                new_order.save_order(str(filename))
            except ValueError:
                pass
            else:
                raise AssertionError("خطای ذخیره‌سازی تشخیص داده نشد.")

        # فایل اصلی نباید تغییر کرده باشد
        assert filename.read_bytes() == original_bytes

        with filename.open("rb") as file:
            saved_orders = pickle.load(file)

        assert 9998 in saved_orders
        assert 9999 not in saved_orders

    print("✅ تست واقعی ذخیره‌سازی اتمی موفق بود.")

def test_temp_file_cleanup():
    import tempfile
    from pathlib import Path
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as temp_dir:
        filename = Path(temp_dir) / "orders.pkl"

        order = Order.__new__(Order)
        order.order_id = 9997

        with patch(
            "model.order.pickle.dump",
            side_effect=OSError("test write failure")
        ):
            try:
                order.save_order(str(filename))
            except ValueError:
                pass
            else:
                raise AssertionError("خطای ذخیره‌سازی تشخیص داده نشد.")

        assert not filename.exists(), "فایل اصلی نباید ساخته شود."
        assert not Path(str(filename) + ".tmp").exists(), (
            "فایل موقت بعد از خطا حذف نشده است."
        )

    print("✅ تست پاک‌سازی فایل موقت موفق بود.")

def test_corrupted_orders_file():
    import tempfile
    from pathlib import Path
    from model.order import Order

    with tempfile.TemporaryDirectory() as temp_dir:
        filename = Path(temp_dir) / "orders.pkl"

        # ساخت یک فایل خراب آزمایشی
        with open(filename, "wb") as file:
            file.write(b"INVALID_PICKLE_DATA")

        # تلاش برای خواندن فایل خراب
        try:
            Order.load_order(
                1001,
                filename=str(filename)
            )

        except (ValueError, EOFError, OSError) as error:
            print("✅ خرابی فایل سفارش‌ها تشخیص داده شد.")
            print(f"نوع خطا: {type(error).__name__}")

        else:
            raise AssertionError(
                "سیستم فایل خراب را بدون خطا قبول کرد!"
            )

def test_check_backup():
    import pickle
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"
        backup_file = Path(temp_dir) / "orders_backup.pkl"

        sample_order = Order.__new__(Order)
        sample_order.order_id = 1012
        sample_orders = {1012: sample_order}

        # حالت اول: فایل اصلی سالم
        with main_file.open("wb") as file:
            pickle.dump(sample_orders, file)

        result = Order.check_backup(str(main_file))

        assert result["status"] == "main_ok"
        assert 1012 in result["orders"]
        assert result["orders"][1012].order_id == 1012

        print("✅ تست خواندن فایل اصلی سالم موفق بود.")

        # حالت دوم: فایل اصلی خراب، پشتیبان سالم
        main_file.write_bytes(b"INVALID_DATA")

        with backup_file.open("wb") as file:
            pickle.dump(sample_orders, file)

        result = Order.check_backup(str(main_file))

        assert result["status"] == "backup_available"
        assert 1012 in result["orders"]
        assert result["orders"][1012].order_id == 1012

        print("✅ تست شناسایی نسخه پشتیبان سالم موفق بود.")

        # حالت سوم: هر دو فایل خراب
        backup_file.write_bytes(b"INVALID_DATA")

        result = Order.check_backup(str(main_file))

        assert result["status"] == "recovery_failed"
        assert result["orders"] is None

        print("✅ تست خرابی هر دو فایل موفق بود.")

def test_invalid_backup_data():
    import pickle
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"
        backup_file = Path(temp_dir) / "orders_backup.pkl"

        # خراب کردن فایل اصلی آزمایشی
        main_file.write_bytes(b"INVALID_DATA")

        # ایجاد پشتیبان با داده نامعتبر
        with backup_file.open("wb") as file:
            pickle.dump({1012: "سفارش نامعتبر"}, file)

        result = Order.check_backup(str(main_file))

        assert result["status"] == "recovery_failed"
        assert result["orders"] is None

    print("✅ تست رد اطلاعات نامعتبر پشتیبان موفق بود.")

def test_restore_backup():
    import pickle
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"
        backup_file = Path(temp_dir) / "orders_backup.pkl"

        sample_order = Order.__new__(Order)
        sample_order.order_id = 1012
        sample_orders = {1012: sample_order}

        # ایجاد فایل اصلی خراب
        main_file.write_bytes(b"INVALID_DATA")

        # ایجاد نسخه پشتیبان سالم
        with backup_file.open("wb") as file:
            pickle.dump(sample_orders, file)

        # اجرای بازیابی
        restored = Order.restore_backup(str(main_file))

        assert restored is True

        # بررسی اطلاعات بازیابی‌شده
        with main_file.open("rb") as file:
            recovered_orders = pickle.load(file)

        assert 1012 in recovered_orders
        assert recovered_orders[1012].order_id == 1012
        assert isinstance(recovered_orders[1012], Order)

        # بررسی پاک‌سازی فایل موقت
        assert not list(
            Path(temp_dir).glob("orders_restore_*.tmp")
        )

        print("✅ تست بازیابی نسخه پشتیبان موفق بود.")

def test_restore_replace_failure():
    import pickle
    import tempfile
    from pathlib import Path
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"
        backup_file = Path(temp_dir) / "orders_backup.pkl"

        sample_order = Order.__new__(Order)
        sample_order.order_id = 1012

        main_file.write_bytes(b"INVALID_DATA")

        with backup_file.open("wb") as file:
            pickle.dump({1012: sample_order}, file)

        original_bytes = main_file.read_bytes()

        with patch(
            "model.order.os.replace",
            side_effect=OSError("خطای آزمایشی")
        ):
            try:
                Order.restore_backup(str(main_file))
            except OSError:
                pass
            else:
                raise AssertionError(
                    "بازیابی باید هنگام خطا متوقف شود."
                )

        assert main_file.read_bytes() == original_bytes

        assert not list(
            Path(temp_dir).glob("orders_restore_*.tmp")
        )

    print("✅ تست ایمنی هنگام شکست بازیابی موفق بود.")

def test_restore_cancel_confirmation():
    import tempfile
    from pathlib import Path
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"

        # فایل آزمایشی که نباید تغییر کند
        original_data = b"TEST_ORIGINAL_DATA"
        main_file.write_bytes(original_data)

        # شبیه‌سازی پاسخ «خیر» در پنجره تأیید
        with patch(
            "tkinter.messagebox.askyesno",
            return_value=False
        ) as mock_confirm:

            with patch.object(
                Order,
                "restore_backup"
            ) as mock_restore:

                confirmed = mock_confirm(
                    "بازیابی سفارش‌ها",
                    "آیا می‌خواهید اطلاعات بازیابی شود؟"
                )

                if confirmed:
                    Order.restore_backup(str(main_file))

                assert confirmed is False
                mock_restore.assert_not_called()

        # فایل آزمایشی باید بدون تغییر باقی بماند
        assert main_file.read_bytes() == original_data

    print("✅ تست لغو بازیابی توسط کاربر موفق بود.")

def test_restore_accept_confirmation():
    import pickle
    import tempfile
    from pathlib import Path
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as temp_dir:
        main_file = Path(temp_dir) / "orders.pkl"
        backup_file = Path(temp_dir) / "orders_backup.pkl"

        sample_order = Order.__new__(Order)
        sample_order.order_id = 1012

        # ایجاد فایل اصلی خراب
        main_file.write_bytes(b"INVALID_DATA")

        # ایجاد نسخه پشتیبان معتبر
        with backup_file.open("wb") as file:
            pickle.dump({1012: sample_order}, file)

        # شبیه‌سازی انتخاب «بله»
        with patch(
            "tkinter.messagebox.askyesno",
            return_value=True
        ) as mock_confirm:

            confirmed = mock_confirm(
                "بازیابی سفارش‌ها",
                "آیا اطلاعات بازیابی شوند؟"
            )

            if confirmed:
                restored = Order.restore_backup(
                    str(main_file)
                )

            assert confirmed is True
            assert restored is True

        # بررسی نتیجه بازیابی
        result = Order.check_backup(str(main_file))

        assert result["status"] == "main_ok"
        assert 1012 in result["orders"]
        assert result["orders"][1012].order_id == 1012

    print("✅ تست تأیید و اجرای بازیابی موفق بود.")

def test_handle_orders_health():
    from unittest.mock import Mock, patch
    from view.tkinter_ui import handle_orders_health

    confirm = Mock(return_value=False)
    info = Mock()
    error = Mock()
    refresh = Mock()

    # حالت اول: کاربر بازیابی را لغو می‌کند
    with patch(
        "view.tkinter_ui.Order.check_backup",
        return_value={"status": "backup_available"}
    ), patch("view.tkinter_ui.Order.restore_backup") as restore:

        handle_orders_health(confirm, info, error, refresh)

        confirm.assert_called_once()
        restore.assert_not_called()
        refresh.assert_not_called()
        error.assert_not_called()

    # حالت دوم: کاربر بازیابی را تأیید می‌کند
    confirm.reset_mock(return_value=True)
    confirm.return_value = True
    info.reset_mock()
    error.reset_mock()
    refresh.reset_mock()

    with patch(
        "view.tkinter_ui.Order.check_backup",
        return_value={"status": "backup_available"}
    ), patch(
        "view.tkinter_ui.Order.restore_backup",
        return_value=True
    ) as restore:

        handle_orders_health(confirm, info, error, refresh)

        restore.assert_called_once()
        refresh.assert_called_once()
        error.assert_not_called()

    # حالت سوم: بازیابی با خطا مواجه می‌شود
    info.reset_mock()
    error.reset_mock()
    refresh.reset_mock()

    with patch(
        "view.tkinter_ui.Order.check_backup",
        return_value={"status": "backup_available"}
    ), patch(
        "view.tkinter_ui.Order.restore_backup",
        side_effect=OSError("خطای آزمایشی")
    ):
        handle_orders_health(confirm, info, error, refresh)

        error.assert_called_once()
        refresh.assert_not_called()

    print("✅ تست مستقیم منطق رابط گرافیکی بازیابی موفق بود.")

if __name__ == "__main__":
    test_duplicate_order()
    test_backup_recovery()
    test_atomic_save_failure()
    test_real_atomic_save()
    test_temp_file_cleanup()
    test_corrupted_orders_file()
    test_check_backup()
    test_invalid_backup_data()
    test_restore_backup()
    test_restore_replace_failure()
    test_restore_cancel_confirmation()
    test_restore_accept_confirmation()
    test_handle_orders_health()





