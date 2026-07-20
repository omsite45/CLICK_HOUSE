from faker import Faker
import os
import pandas as pd
import random
from dataset_generator.categories import PRODUCT_CATEGORIES
fake = Faker()


class RetailDataGenerator:

    def __init__(self):

        self.fake = fake

        self.output_dir = "datasets"

        os.makedirs(self.output_dir, exist_ok=True)


    def generate_suppliers(self):

        print("Generating suppliers...")

        countries = [
            "USA",
            "Germany",
            "Japan",
            "China",
            "India",
            "UK",
            "France",
            "Italy",
            "South Korea",
            "Canada"
        ]

        supplier_prefixes = [
            "Global",
            "Prime",
            "NextGen",
            "Elite",
            "Vertex",
            "Future",
            "United",
            "National",
            "Advanced",
            "Dynamic"
        ]

        supplier_suffixes = [
            "Technologies",
            "Industries",
            "Solutions",
            "Trading",
            "Electronics",
            "Retail",
            "Manufacturing",
            "Distribution",
            "Supply",
            "Logistics"
        ]

        rows = []

        for supplier_id in range(1, 2001):

            company = (
                random.choice(supplier_prefixes)
                + " "
                + random.choice(supplier_suffixes)
            )

            rows.append({

                "supplier_id": supplier_id,

                "supplier_name": company,

                "country": random.choice(countries),

                "contact_email": f"sales{supplier_id}@example.com",

                "phone": self.fake.phone_number(),

                "rating": round(random.uniform(3.5, 5.0), 2)

            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/suppliers.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} suppliers")



    def generate_warehouses(self):

        print("Generating warehouses...")

        warehouse_names = [
            "North Hub",
            "South Hub",
            "East Hub",
            "West Hub",
            "Central Hub",
            "Primary Distribution",
            "Regional DC",
            "Metro Warehouse",
            "Express Hub",
            "Logistics Center",
            "Smart Warehouse",
            "National Depot",
            "Mega Storage",
            "Retail Fulfillment",
            "International Hub",
            "City Warehouse",
            "Global Warehouse",
            "Premium Storage",
            "Supply Center",
            "Main Distribution"
        ]

        cities = [
            "New York",
            "Chicago",
            "Dallas",
            "Los Angeles",
            "Seattle",
            "London",
            "Berlin",
            "Paris",
            "Tokyo",
            "Singapore",
            "Dubai",
            "Mumbai",
            "Toronto",
            "Sydney",
            "Amsterdam",
            "Riyadh",
            "Jeddah",
            "Doha",
            "Bangalore",
            "Seoul"
        ]

        countries = [
            "USA",
            "USA",
            "USA",
            "USA",
            "USA",
            "UK",
            "Germany",
            "France",
            "Japan",
            "Singapore",
            "UAE",
            "India",
            "Canada",
            "Australia",
            "Netherlands",
            "Saudi Arabia",
            "Saudi Arabia",
            "Qatar",
            "India",
            "South Korea"
        ]

        rows = []

        for warehouse_id in range(1, 21):

            rows.append({
                "warehouse_id": warehouse_id,
                "warehouse_name": warehouse_names[warehouse_id - 1],
                "city": cities[warehouse_id - 1],
                "country": countries[warehouse_id - 1],
                "capacity": random.randint(50000, 250000)
            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/warehouses.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} warehouses")


    

    def generate_customers(self):

        print("Generating customers...")

        segments = ["Bronze", "Silver", "Gold", "Platinum"]

        countries = [
            "USA",
            "Canada",
            "UK",
            "Germany",
            "France",
            "India",
            "Japan",
            "Australia",
            "Saudi Arabia",
            "UAE"
        ]

        rows = []

        for customer_id in range(1, 50001):

            profile = fake.simple_profile()

            rows.append({

                "customer_id": customer_id,

                "first_name": profile["name"].split()[0],

                "last_name": profile["name"].split()[-1],

                "email": f"customer{customer_id}@example.com",

                "phone": fake.phone_number(),

                "gender": profile["sex"],

                "date_of_birth": profile["birthdate"],

                "city": fake.city(),

                "state": fake.state(),

                "country": random.choice(countries),

                "postal_code": fake.postcode(),

                "signup_date": fake.date_between(
                    start_date="-5y",
                    end_date="today"
                ),

                "customer_segment": random.choices(
                    segments,
                    weights=[45, 30, 20, 5],
                    k=1
                )[0]

            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/customers.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} customers")


    def generate_products(self):

        print("Generating products...")

        colors = [
            "Black",
            "White",
            "Silver",
            "Blue",
            "Gray",
            "Red"
        ]

        rows = []

        product_id = 1

        while product_id <= 10000:

            category = random.choice(list(PRODUCT_CATEGORIES.keys()))

            subcategory = random.choice(
                list(PRODUCT_CATEGORIES[category].keys())
            )

            brand = random.choice(
                PRODUCT_CATEGORIES[category][subcategory]
            )

            product_name = f"{brand} {subcategory} {random.randint(100,9999)}"

            description = (
                f"{brand} {subcategory} designed for high performance "
                f"and everyday use. Premium quality with modern features."
            )

            rows.append({

                "product_id": product_id,

                "product_name": product_name,

                "brand": brand,

                "category": category,

                "subcategory": subcategory,

                "description": description,

                "price": round(
                    random.uniform(20, 2500),
                    2
                ),

                "cost": round(
                    random.uniform(10, 1800),
                    2
                ),

                "color": random.choice(colors),

                "weight_kg": round(
                    random.uniform(0.2, 20),
                    2
                ),

                "rating": round(
                    random.uniform(3.5, 5.0),
                    1
                ),

                "supplier_id": random.randint(1, 2000)

            })

            product_id += 1

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/products.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} products")




    def generate_orders(self):

        print("Generating orders...")

        order_statuses = [
            "Pending",
            "Processing",
            "Shipped",
            "Delivered",
            "Cancelled"
        ]

        cities = [
            "New York",
            "Chicago",
            "Dallas",
            "Los Angeles",
            "Seattle",
            "London",
            "Berlin",
            "Paris",
            "Tokyo",
            "Singapore",
            "Dubai",
            "Mumbai",
            "Toronto",
            "Sydney",
            "Amsterdam",
            "Riyadh"
        ]

        countries = [
            "USA",
            "USA",
            "USA",
            "USA",
            "USA",
            "UK",
            "Germany",
            "France",
            "Japan",
            "Singapore",
            "UAE",
            "India",
            "Canada",
            "Australia",
            "Netherlands",
            "Saudi Arabia"
        ]

        rows = []

        for order_id in range(1, 250001):

            order_date = self.fake.date_time_between(
                start_date="-3y",
                end_date="now"
            )

            shipping_cost = round(random.uniform(5, 50), 2)

            discount = round(random.uniform(0, 100), 2)

            total_amount = round(random.uniform(50, 5000), 2)

            city_index = random.randint(0, len(cities) - 1)

            rows.append({

                "order_id": order_id,

                "customer_id": random.randint(1, 50000),

                "order_date": order_date,

                "status": random.choices(
                    order_statuses,
                    weights=[5, 10, 15, 65, 5],
                    k=1
                )[0],

                "shipping_city": cities[city_index],

                "shipping_country": countries[city_index],

                "shipping_cost": shipping_cost,

                "discount": discount,

                "total_amount": total_amount

            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/orders.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} orders")


    def generate_order_items(self):

        print("Generating order items...")

        # Load product catalog to get prices
        products = pd.read_csv("datasets/products.csv")

        product_price = dict(zip(products.product_id, products.price))

        rows = []

        order_item_id = 1

        # One order can have multiple products
        for order_id in range(1, 250001):

            num_items = random.randint(1, 5)

            selected_products = random.sample(
                range(1, 10001),
                num_items
            )

            for product_id in selected_products:

                quantity = random.randint(1, 5)

                unit_price = float(product_price[product_id])

                discount_pct = random.choice([0, 5, 10, 15, 20])

                discount_amount = round(
                    unit_price * quantity * discount_pct / 100,
                    2
                )

                total_price = round(
                    unit_price * quantity - discount_amount,
                    2
                )

                rows.append({

                    "order_item_id": order_item_id,

                    "order_id": order_id,

                    "product_id": product_id,

                    "quantity": quantity,

                    "unit_price": unit_price,

                    "discount_pct": discount_pct,

                    "discount_amount": discount_amount,

                    "total_price": total_price

                })

                order_item_id += 1

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/order_items.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} order items")



    def generate_payments(self):

        print("Generating payments...")

        orders = pd.read_csv("datasets/orders.csv")

        payment_methods = [
            "Credit Card",
            "Debit Card",
            "PayPal",
            "Apple Pay",
            "Google Pay",
            "Bank Transfer"
        ]

        payment_statuses = [
            "Completed",
            "Pending",
            "Failed",
            "Refunded"
        ]

        rows = []

        transaction_id = 1

        for _, order in orders.iterrows():

            amount = round(float(order["total_amount"]), 2)

            status = random.choices(
                payment_statuses,
                weights=[90, 5, 3, 2],
                k=1
            )[0]

            rows.append({

                "payment_id": transaction_id,

                "order_id": int(order["order_id"]),

                "payment_method": random.choice(payment_methods),

                "payment_status": status,

                "payment_date": order["order_date"],

                "amount": amount,

                "currency": "USD",

                "transaction_reference": f"TXN{transaction_id:010d}"

            })

            transaction_id += 1

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/payments.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} payments")



    def generate_inventory(self):

        print("Generating inventory...")

        products = pd.read_csv("datasets/products.csv")

        rows = []

        inventory_id = 1

        for warehouse_id in range(1, 21):

            for _, product in products.iterrows():

                quantity = random.randint(0, 500)

                reorder_level = random.randint(20, 80)

                max_stock = random.randint(500, 1000)

                rows.append({

                    "inventory_id": inventory_id,

                    "warehouse_id": warehouse_id,

                    "product_id": int(product["product_id"]),

                    "quantity_on_hand": quantity,

                    "reorder_level": reorder_level,

                    "max_stock": max_stock,

                    "unit_cost": round(float(product["cost"]), 2),

                    "inventory_value": round(
                        quantity * float(product["cost"]),
                        2
                    )

                })

                inventory_id += 1

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/inventory.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} inventory records")



    def generate_reviews(self):

        print("Generating reviews...")

        review_titles = [
            "Excellent Product",
            "Highly Recommended",
            "Very Good",
            "Worth the Money",
            "Average Experience",
            "Not Bad",
            "Fantastic Quality",
            "Exceeded Expectations",
            "Good Value",
            "Could Be Better"
        ]

        positive_reviews = [
            "Excellent build quality and fast delivery.",
            "Very satisfied with this purchase.",
            "Works exactly as described.",
            "Highly recommend this product.",
            "Outstanding quality and performance.",
            "Amazing product for the price.",
            "Five stars without hesitation.",
            "Customer service was excellent.",
            "Packaging was secure and delivery was quick.",
            "Would definitely buy again."
        ]

        neutral_reviews = [
            "The product is okay overall.",
            "Average quality for the price.",
            "Delivery was slightly delayed.",
            "Works fine but expected more.",
            "Good but not exceptional."
        ]

        negative_reviews = [
            "Product arrived damaged.",
            "Not worth the price.",
            "Poor build quality.",
            "Stopped working after a few days.",
            "Would not recommend."
        ]

        rows = []

        review_id = 1

        for _ in range(150000):

            rating = random.randint(1, 5)

            if rating >= 4:
                review = random.choice(positive_reviews)
            elif rating == 3:
                review = random.choice(neutral_reviews)
            else:
                review = random.choice(negative_reviews)

            rows.append({

                "review_id": review_id,

                "customer_id": random.randint(1, 50000),

                "product_id": random.randint(1, 10000),

                "rating": rating,

                "review_title": random.choice(review_titles),

                "review_text": review,

                "verified_purchase": random.choice([True, False]),

                "review_date": self.fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )

            })

            review_id += 1

        df = pd.DataFrame(rows)

        df.to_csv(
            "datasets/reviews.csv",
            index=False
        )

        print(f"✓ Generated {len(df)} reviews")

    def generate_all(self):

        self.generate_suppliers()

        self.generate_warehouses()

        self.generate_customers()

        self.generate_products()

        self.generate_orders()

        self.generate_order_items()

        self.generate_payments()

        self.generate_inventory()

        self.generate_reviews()

        print("\nDataset generation completed.")