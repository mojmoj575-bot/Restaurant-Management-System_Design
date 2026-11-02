from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from datetime import datetime
from tkinter import filedialog, messagebox
import os


def export_orders_to_excel(orders_admin_table):
    try:
        file_path = filedialog.asksaveasfilename(
            title="ذخیره گزارش سفارش‌ها",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            initialfile="restaurant_orders.xlsx"
        )

        if not file_path:
            return

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "سفارش‌ها"
        sheet.sheet_view.rightToLeft = True

        sheet.merge_cells("A1:C1")
        sheet["A1"] = "گزارش فروش رستوران"

        sheet["A1"].font = Font(
            name="Tahoma",
            size=16,
            bold=True,
            color="FFFFFF"
        )

        sheet["A1"].fill = PatternFill(
            fill_type="solid",
            fgColor="243B55"
        )

        sheet["A1"].alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

        sheet.row_dimensions[1].height = 35

        sheet.merge_cells("A2:C2")
        sheet["A2"] = (
                "تاریخ تهیه گزارش: "
                + datetime.now().strftime("%Y/%m/%d")
        )

        sheet["A2"].alignment = Alignment(
            horizontal="center"
        )

        sheet.append([])
        sheet.append([])
        sheet.append([])
        sheet.append([
            "شماره سفارش",
            "نام مشتری",
            "مبلغ کل (تومان)"
        ])

        for item_id in orders_admin_table.get_children():
            values = orders_admin_table.item(
                item_id, "values"
            )

            sheet.append([
                int(values[0]),
                values[1],
                int(str(values[2]).replace(",", ""))
            ])

        for cell in sheet[6]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(
                fill_type="solid",
                fgColor="243B55"
            )
            cell.alignment = Alignment(
                horizontal="center"
            )

        sheet.column_dimensions["A"].width = 20
        sheet.column_dimensions["B"].width = 30
        sheet.column_dimensions["C"].width = 25

        for row in sheet.iter_rows(min_row=7):
            for cell in row:
                cell.alignment = Alignment(
                    horizontal="center"
                )
            row[2].number_format = "#,##0"

        order_count = len(orders_admin_table.get_children())

        total_sales = sum(
            sheet.cell(row=i, column=3).value
            for i in range(5, sheet.max_row + 1)
            if isinstance(
                sheet.cell(row=i, column=3).value,
                (int, float)
            )
        )

        average_sales = (
            total_sales / order_count
            if order_count > 0 else 0
        )

        summary_row = sheet.max_row + 2

        sheet.cell(
            row=summary_row,
            column=2,
            value="تعداد سفارش‌ها"
        )
        sheet.cell(
            row=summary_row,
            column=3,
            value=order_count
        )

        sheet.cell(
            row=summary_row + 1,
            column=2,
            value="مجموع فروش (تومان)"
        )
        sheet.cell(
            row=summary_row + 1,
            column=3,
            value=total_sales
        )

        sheet.cell(
            row=summary_row + 2,
            column=2,
            value="میانگین سفارش (تومان)"
        )
        sheet.cell(
            row=summary_row + 2,
            column=3,
            value=average_sales
        )

        for row in range(summary_row, summary_row + 3):
            sheet.cell(row=row, column=2).font = Font(bold=True)
            sheet.cell(row=row, column=3).font = Font(bold=True)
            sheet.cell(
                row=row,
                column=3
            ).number_format = "#,##0"

        sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
        sheet.page_setup.orientation = "portrait"
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 1

        sheet.print_options.horizontalCentered = True
        sheet.print_area = f"A1:C{sheet.max_row}"

        sheet.page_margins.left = 0.3
        sheet.page_margins.right = 0.3
        sheet.page_margins.top = 0.5
        sheet.page_margins.bottom = 0.5

        sheet.row_dimensions[6].height = 30

        for row in range(7, summary_row - 1):
            sheet.row_dimensions[row].height = 28

            for cell in sheet[row][:3]:
                cell.font = Font(
                    name="Tahoma",
                    size=13
                )
                cell.alignment = Alignment(
                    horizontal="center",
                    vertical="center"
                )

        for row in range(summary_row, summary_row + 3):
            sheet.row_dimensions[row].height = 30

            for cell in sheet[row][1:3]:
                cell.font = Font(
                    name="Tahoma",
                    size=12,
                    bold=True
                )

        workbook.save(file_path)

        messagebox.showinfo(
            "خروجی اکسل",
            "فایل اکسل با موفقیت ذخیره شد."
        )

    except (OSError, ValueError, IndexError) as error:
        messagebox.showerror(
            "خطا در خروجی اکسل",
            str(error)
        )