import csv
import random
from datetime import datetime, timedelta

# Config
num_customers = 10000
num_products = 1000
num_returns = 100000
start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-06-30", "%Y-%m-%d")
days_range = (end_date - start_date).days

# Sample lists
regions = ["North", "South", "East", "West", "Central"]
loyalty_statuses = ["Bronze", "Silver", "Gold", "Platinum"]
categories = ["Electronics", "Books", "Home", "Apparel", "Toys", "Grocery", "Automotive"]
reasons = ["Defective", "Wrong Item", "No longer needed", "Late delivery", "Changed mind", "Better price elsewhere"]

# === Generate customers.csv ===
# with open("customers.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["customer_id", "region", "loyalty_status"])
#     for i in range(1000, 1000 + num_customers):
#         writer.writerow([i, random.choice(regions), random.choice(loyalty_statuses)])

# # === Generate products.csv ===
# with open("products.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["product_id", "category", "cost", "name"])
#     for i in range(500, 500 + num_products):
#         cost = round(random.uniform(10, 500), 2)
#         writer.writerow([i, random.choice(categories), cost, f"Product_{i}"])

# === Generate returns.csv ===
with open("returns.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["return_id", "product_id", "customer_id", "return_date", "reason", "refund_amount"])
    for i in range(1, num_returns + 1):
        product_id = random.randint(500, 499 + num_products)
        customer_id = random.randint(1000, 999 + num_customers)
        return_date = start_date + timedelta(days=random.randint(0, days_range))
        reason = random.choice(reasons)
        refund_amount = round(random.uniform(5.00, 500.00), 2)
        writer.writerow([i, product_id, customer_id, return_date.strftime("%Y-%m-%d"), reason, refund_amount])
