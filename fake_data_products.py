from faker import Faker
import random
from datetime import timedelta
fake = Faker()

categories = [
    "Sữa tươi", "Sữa chua", "Sữa đặc", "Sữa hạt", 
    "Sữa công thức", "Sữa không đường", "Sữa hữu cơ"
]

origins = ["Việt Nam", "Mỹ", "Úc", "New Zealand", "Hà Lan", "Nhật Bản", "Đức", "Thái Lan"]

brands = [
    "Vinamilk", "TH True Milk", "Nutifood", "Dutch Lady", 
    "Nestlé", "Morinaga", "Meiji", "Ensure", 
    "Friso", "Abbott", "Colosbaby", "GrowPLUS+", 
    "Anlene", "Fami", "Ovaltine", "Milo", "Lactel", "Love’in Farm"
]

types = [
    "Sữa tươi tiệt trùng", "Sữa chua uống", "Sữa đặc có đường", 
    "Sữa hạt óc chó", "Sữa hạnh nhân", "Sữa công thức", 
    "Sữa bột pha sẵn", "Sữa không lactose", "Sữa hữu cơ"
]

variants = [
    "1L", "180ml", "200ml", "Có đường", "Ít đường", 
    "Không đường", "Hương Dâu", "Hương Chuối", 
    "Hương Socola", "Gold", "Organic", "Dành cho bé", 
    "Người lớn tuổi", "Dinh dưỡng cao"
]

def generate_product_id(i):
    return f"P{i:04d}"

def generate_cost_and_price():
    cost = round(random.uniform(10_000, 50_000), -2)
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

print("✅ Đã tạo file insert_product_data.txt chứa 1000 dòng dữ liệu.")
