import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


def menu():
    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")

def view_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - "
            f"{item['price']:,} VNĐ"
        )

def add_to_order(current_order):
    print("\n--- THÊM MÓN VÀO GIỎ ---")
    drink_code = input("Nhập mã đồ uống: ").strip().upper()
    try:
        if drink_code not in DRINK_MENU:
            logging.warning(
                f"ItemNotFoundError - Code: {drink_code}"
            )
            raise ValueError(
                "Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!"
            )
        quantity = int(input("Nhập số lượng: "))
        if quantity <= 0:
            logging.warning(
                f"InvalidQuantityError - Quantity: {quantity}"
            )
            raise ValueError(
                "Số lượng phải lớn hơn 0!"
            )
        current_order.append(
            {
                "code": drink_code,
                "quantity": quantity
            }
        )
        logging.info(
            f"Added {quantity} of {drink_code} to order"
        )
        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[drink_code]['name']} "
            f"vào giỏ hàng."
        )

    except ValueError as e:
        error_msg = str(e)
        if "invalid literal for int()" in error_msg:
            print("Vui lòng nhập số lượng là một số nguyên!")
            logging.error(
                "ValueError - Invalid quantity input"
            )
        else:
            print(error_msg)
    return current_order

def calculate_total(current_order):
    total = 0
    for item in current_order:
        total += (
            DRINK_MENU[item["code"]]["price"]
            * item["quantity"]
        )
    return total

def view_order(current_order):
    if len(current_order) == 0:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return
    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(
        f"{'Mã SP':<6} | "
        f"{'Tên đồ uống':<20} | "
        f"{'Đơn giá':<10} | "
        f"{'Số lượng':<8} | "
        f"Thành tiền"
    )
    for item in current_order:
        code = item["code"]
        quantity = item["quantity"]
        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]
        amount = price * quantity
        print(
            f"{code:<6} | "
            f"{name:<20} | "
            f"{price:<10,} | "
            f"{quantity:<8} | "
            f"{amount:,} VNĐ"
        )
    print("-" * 70)
    print(
        f"Tổng tiền cần thanh toán: "
        f"{calculate_total(current_order):,} VNĐ"
    )

def checkout(current_order):
    if len(current_order) == 0:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return
    total = calculate_total(current_order)
    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()
    if confirm == "y":
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        current_order.clear()
        print("Giỏ hàng đã được làm trống.")
    elif confirm == "n":
        print(
            "Đã hủy thao tác thanh toán. Quay lại menu chính."
        )
    else:
        print(
            "Lựa chọn không hợp lệ. Thanh toán đã bị hủy."
        )

def main():
    current_order = []
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ")
        match choice:
            case "1":
                view_menu()

            case "2":
                current_order = add_to_order(current_order)

            case "3":
                view_order(current_order)

            case "4":
                checkout(current_order)

            case "5":
                logging.info(
                    "Cashier logged out. System shutdown."
                )

                print(
                    "Đã thoát ca làm việc. Hẹn gặp lại!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()