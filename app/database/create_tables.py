from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, MetaData
from app.database.connection import get_engine

# Create metadata object
metadata = MetaData()

# Define tables
customers = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("city", String),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("price", Float),
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("total_amount", Float),
)

order_items = Table(
    "order_items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer),
)


def create_tables():
    engine = get_engine()
    metadata.create_all(engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()