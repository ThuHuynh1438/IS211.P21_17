from faker import Faker
import random

fake = Faker()

def generate_invoice_data(store_id: str, store_code: str, count: int):
    invoice_file = f"invoice_{store_id.lower()}.txt"
    item_file = f"invoice_item_{store_id.lower()}.txt"

    with open(invoice_file, "w", encoding="utf-8") as inv_f, open(item_file, "w", encoding="utf-8") as item_f:
        for i in range(1, count + 1):
            invoice_id = f"{store_code}_{i:06d}"
            staff_id = f"S{random.randint(1, 1000):04d}"
            customer_id = f"CUST{random.randint(1, 1000):04d}"
            invoice_date = fake.date_between(start_date='-1y', end_date='today')
            
            # Random total amount
            item_count = 1 if random.random() < 0.6 else 2
            items = []
            total = 0
            for _ in range(item_count):
                product_id = f"P{random.randint(1, 1000):04d}"
                quantity = random.randint(1, 10)
                price = random.randint(20000, 100000)
                total += quantity * price
                items.append((invoice_id, product_id, quantity))

            # Ghi INVOICE
            inv_stmt = f"INSERT INTO INVOICE (INVOICE_ID, STAFF_ID, CUSTOMER_ID, INVOICE_DATE, TOTAL_AMOUNT) VALUES ('{invoice_id}', '{staff_id}', '{customer_id}', DATE '{invoice_date}', {total});"
            inv_f.write(inv_stmt + "\n")

            # Ghi INVOICE_ITEM
            for item in items:
                item_stmt = f"INSERT INTO INVOICE_ITEM (INVOICE_ID, PRODUCT_ID, QUANTITY) VALUES ('{item[0]}', '{item[1]}', {item[2]});"
                item_f.write(item_stmt + "\n")

    print(f"✅ Đã tạo xong {invoice_file} và {item_file} với {count} hóa đơn.")

# Ví dụ: Tạo dữ liệu cho STORE1
generate_invoice_data("STORE3", "ST3", 400000)
