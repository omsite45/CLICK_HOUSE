from dataclasses import dataclass

@dataclass
class DatasetConfig:

    NUM_CUSTOMERS = 50_000

    NUM_SUPPLIERS = 2_000

    NUM_PRODUCTS = 10_000

    NUM_ORDERS = 250_000

    NUM_ORDER_ITEMS = 1_000_000

    NUM_PAYMENTS = 250_000

    NUM_REVIEWS = 150_000

    NUM_WAREHOUSES = 20

    NUM_INVENTORY = 20_000