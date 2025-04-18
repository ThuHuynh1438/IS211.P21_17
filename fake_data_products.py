from faker import Faker
import random
from datetime import timedelta

fake = Faker()

categories = [
    "Sua tuoi", "Sua chua", "Sua dac", "Sua hat", 
    "Sua cong thuc", "Sua khong duong", "Sua huu co"
]

origins = ["Viet Nam", "My", "Uc", "New Zealand", "Ha Lan", "Nhat Ban", "Duc", "Thai Lan"]

brands = [
    "Vinamilk", "TH True Milk", "Nutifood", "Dutch Lady", 
    "Nestle", "Morinaga", "Meiji", "Ensure", 
    "Friso", "Abbott", "Colosbaby", "GrowPLUS", 
    "Anlene", "Fami", "Ovaltine", "Milo", "Lactel", "Lovein Farm"
]

types = [
    "Sua tuoi tiet trung", "Sua chua uong", "Sua dac co duong", 
    "Sua hat oc cho", "Sua hanh nhan", "Sua cong thuc", 
    "Sua bot pha san", "Sua khong lactose", "Sua huu co"
]

variants = [
    "1L", "180ml", "200ml", "Co duong", "It duong", 
    "Khong duong", "Huong Dau", "Huong Chuoi", 
    "Huong Socola", "Gold", "Organic", "Danh cho be", 
    "Nguoi lon tuoi", "Dinh duong cao"
]

def generate_product_id(i):
    return f"P{i:04d}"

def generate_cost_and_price():
    cost = round(random.uniform(10000, 50000), -2)
    price = round(cost * random.uniform(1.1, 1.5), -2)
    return cost, price

def generate_dates():
    prod_date = fake.date_between(start_date='-1y', end_date='today')
    expiry_date = prod_date + timedelta(days=random.randint(120, 365))
    return prod_date, expiry_date

def generate_product(i):
    product_id = generate_product_id(i)
    name = f"{random.choice(brands)} {random.choice(types)} {random.choice(variants)}"
    origin = random.choice(origins)
    cost_price, selling_price = generate_cost_and_price()
    prod_date, expiry_date = generate_dates()
    category = random.choice(categories)
    vat = random.choice([5, 8, 10])
    stock = random.randint(0, 500)
    return f"INSERT INTO PRODUCT (PRODUCT_ID, PRODUCT_NAME, ORIGIN, COST_PRICE, SELLING_PRICE, PRODUCTION_DATE, EXPIRY_DATE, CATEGORY, VAT, STOCK) VALUES ('{product_id}', '{name}', '{origin}', {cost_price}, {selling_price}, DATE '{prod_date}', DATE '{expiry_date}', '{category}', {vat}, {stock});"

# Tạo ra file txt
filename = f"insert_product_data.txt"
with open(filename, "w", encoding="utf-8") as f:
    for i in range(1, 1001):
        insert_stmt = generate_product(i)
        f.write(insert_stmt + "\n")

print("✅ Đã tạo file insert_product_data.txt chứa 1000 dòng dữ liệu KHÔNG DẤU.")
