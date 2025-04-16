import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# --- Số bản ghi cần tạo ---
NUM_SUPPORT = 1000  # Các bảng hỗ trợ
NUM_TRANSACTIONS = 1000000  # 1 triệu giao dịch
NUM_PRODUCTS = 1000  # 1000 sản phẩm

# --- Tạo các danh sách dữ liệu ---
# Danh sách sản phẩm có thật
real_products = [
    "Sữa tươi Vinamilk", "Sữa đặc Ông Thọ", "Sữa chua TH True Milk",
    "Sữa bột Dielac Grow Plus", "Sữa tươi tiệt trùng TH True Milk",
    "Sữa chua uống Probi", "Sữa bột Friso Gold", "Sữa bột Nan Optipro",
    "Sữa chua uống Yakult", "Sữa tươi Dalat Milk", "Sữa tươi Mộc Châu",
    "Sữa bột Meiji", "Sữa bột Abbott Grow", "Sữa bột Enfa A+",
    "Sữa chua Vinamilk nha đam", "Sữa chua men sống Betagen",
    "Sữa óc chó Vegemil", "Sữa bột Ensure Gold", "Sữa tươi Love’in Farm",
    "Sữa hạt TH True Nut", "Sữa đậu nành Fami", "Sữa tươi NutiFood",
    "Sữa tươi Dutch Lady", "Sữa tiệt trùng Zott", "Sữa hạt óc chó Sahmyook"
] * 50  # Giả lập danh sách sản phẩm

# Danh sách tên đường thật (có thể mở rộng thêm nếu cần)
street_names = [
    "Nguyễn Huệ", "Lý Thường Kiệt", "Trần Hưng Đạo", "Hai Bà Trưng", "Cách Mạng Tháng 8",
    "Điện Biên Phủ", "Phan Đăng Lưu", "Trường Chinh", "Hoàng Văn Thụ", "Lê Lợi","Nguyễn Thái Học"
]

# --- Sinh ID ngẫu nhiên ---
def gen_id(prefix, i, total_len=10):
    return f"{prefix}{str(i).zfill(total_len - len(prefix))}"

# --- Sinh địa chỉ ngẫu nhiên ---
def random_address():
    return f"Số {random.randint(1, 300)}, đường {random.choice(street_names)}, {fake.city()}"

# --- Mở file SQL để xuất --
with open('generated_data.sql', 'w', encoding='utf-8') as f:

    # 1. Tạo chi nhánh (STORE)
    f.write("-- INSERT INTO STORE\n")
    branches = []
    for i in range(NUM_SUPPORT):
        store_id = gen_id("CN", i)
        store_name = f"Chi nhánh {i+1}"
        location = random_address().replace("'", "''")
        f.write(f"INSERT INTO STORE (STORE_ID, STORE_NAME, LOCATION) VALUES ('{store_id}', '{store_name}', '{location}');\n")
        branches.append(store_id)

    # 2. Tạo nhân viên (STAFF)
    f.write("\n-- INSERT INTO STAFF\n")
    employees = []
    for i in range(NUM_SUPPORT):
        staff_id = gen_id("NV", i)
        full_name = fake.name()
        gender = random.choice(["Nam", "Nữ"])
        dob = fake.date_of_birth(minimum_age=20, maximum_age=60)
        phone = fake.phone_number()
        address = random_address().replace("'", "''")
        join_date = fake.date_between("-5y", "today")
        salary = round(random.uniform(5000000, 20000000), 2)
        job_title = random.choice(["Nhân viên", "Quản lý"])
        store_id = random.choice(branches)
        f.write(f"INSERT INTO STAFF (STAFF_ID, FULL_NAME, GENDER, DOB, PHONE, ADDRESS, JOIN_DATE, SALARY, JOB_TITLE, STORE_ID) VALUES ('{staff_id}', '{full_name}', '{gender}', DATE '{dob}', '{phone}', '{address}', DATE '{join_date}', {salary}, '{job_title}', '{store_id}');\n")
        employees.append(staff_id)

    # 3. Tạo khách hàng (CUSTOMER)
    f.write("\n-- INSERT INTO CUSTOMER\n")
    customers = []
    for i in range(NUM_SUPPORT):
        customer_id = gen_id("KH", i)
        full_name = fake.name()
        gender = random.choice(["Nam", "Nữ"])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=60)
        phone = fake.phone_number()
        registration_date = fake.date_between("-5y", "today")
        total_spent = round(random.uniform(100000, 5000000), 2)
        loyalty_points = random.randint(0, 500)
        f.write(f"INSERT INTO CUSTOMER (CUSTOMER_ID, FULL_NAME, GENDER, DOB, PHONE, REGISTRATION_DATE, TOTAL_SPENT, LOYALTY_POINTS) VALUES ('{customer_id}', '{full_name}', '{gender}', DATE '{dob}', '{phone}', DATE '{registration_date}', {total_spent}, {loyalty_points});\n")
        customers.append(customer_id)

    # 4. Tạo sản phẩm (PRODUCT)
    f.write("\n-- INSERT INTO PRODUCT\n")
    products = []
    for i in range(NUM_PRODUCTS):
        product_id = gen_id("SP", i)
        product_name = real_products[i]
        origin = fake.country()
        cost_price = round(random.uniform(10000, 500000), 2)
        selling_price = round(cost_price * random.uniform(1.1, 1.5), 2)
        production_date = fake.date_between("-2y", "-1y")
        expiry_date = fake.date_between("+1y", "+3y")
        category = random.choice(["Điện tử", "Văn phòng phẩm", "Thực phẩm", "Đồ gia dụng"])
        vat = random.choice([5, 10, 15])
        stock = random.randint(10, 1000)
        f.write(f"INSERT INTO PRODUCT (PRODUCT_ID, PRODUCT_NAME, ORIGIN, COST_PRICE, SELLING_PRICE, PRODUCTION_DATE, EXPIRY_DATE, CATEGORY, VAT, STOCK) VALUES ('{product_id}', '{product_name}', '{origin}', {cost_price}, {selling_price}, DATE '{production_date}', DATE '{expiry_date}', '{category}', {vat}, {stock});\n")
        products.append(product_id)

    # 5. Quản lý kho (INVENTORY_MANAGEMENT)
    f.write("\n-- INSERT INTO INVENTORY_MANAGEMENT\n")
    for store_id in branches:
        for product_id in products:
            receipt_date = fake.date_between("-1y", "today")
            quantity_received = random.randint(10, 500)
            f.write(f"INSERT INTO INVENTORY_MANAGEMENT (STORE_ID, PRODUCT_ID, RECEIPT_DATE, QUANTITY_RECEIVED) VALUES ('{store_id}', '{product_id}', DATE '{receipt_date}', {quantity_received});\n")

    # 6. Tình trạng bán hàng (INVENTORY_SALES)
    f.write("\n-- INSERT INTO INVENTORY_SALES\n")
    for store_id in branches:
        for product_id in products:
            status = random.choice(["Còn hàng", "Hết hàng", "Sắp hết hàng"])
            f.write(f"INSERT INTO INVENTORY_SALES (STORE_ID, PRODUCT_ID, STATUS) VALUES ('{store_id}', '{product_id}', '{status}');\n")

    # 7. Tạo giao dịch (INVOICE)
    f.write("\n-- INSERT INTO INVOICE\n")
    invoice_item_count = 0  # Biến đếm số lượng bản ghi trong INVOICE_ITEM
    for i in range(NUM_TRANSACTIONS):
        invoice_id = gen_id("HD", i)
        staff_id = random.choice(employees)
        customer_id = random.choice(customers)
        invoice_date = fake.date_between("-1y", "today")
        total_amount = round(random.uniform(100000, 5000000), 2)
        f.write(f"INSERT INTO INVOICE (INVOICE_ID, STAFF_ID, CUSTOMER_ID, INVOICE_DATE, TOTAL_AMOUNT) VALUES ('{invoice_id}', '{staff_id}', '{customer_id}', DATE '{invoice_date}', {total_amount});\n")

        # 8. Tạo chi tiết hóa đơn (INVOICE_ITEM)
        num_items = random.randint(1, 5)  # Mỗi hóa đơn có từ 1 đến 5 sản phẩm
        for _ in range(num_items):
            product_id = random.choice(products)
            quantity = random.randint(1, 5)
            f.write(f"INSERT INTO INVOICE_ITEM (INVOICE_ID, PRODUCT_ID, QUANTITY) VALUES ('{invoice_id}', '{product_id}', {quantity});\n")
            invoice_item_count += 1

    print(f"Total INVOICE_ITEM records generated: {invoice_item_count}")
