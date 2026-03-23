from app.database.connection import get_engine
from sqlalchemy import text


def seed_data():
    engine = get_engine()

    with engine.connect() as conn:

        # Insert customers
        conn.execute(text("""
            INSERT INTO customers (id, name, city) VALUES
            (1, 'Alice', 'New York'),
            (2, 'Bob', 'Chicago'),
            (3, 'Charlie', 'Los Angeles')
        """))

        # Insert products
        conn.execute(text("""
            INSERT INTO products (id, name, price) VALUES
            (1, 'Laptop', 1200.00),
            (2, 'Phone', 800.00),
            (3, 'Headphones', 150.00)
        """))

        # Insert orders
        conn.execute(text("""
            INSERT INTO orders (id, customer_id, total_amount) VALUES
            (1, 1, 1350.00),
            (2, 2, 800.00)
        """))

        # Insert order items
        conn.execute(text("""
            INSERT INTO order_items (id, order_id, product_id, quantity) VALUES
            (1, 1, 1, 1),
            (2, 1, 3, 1),
            (3, 2, 2, 1)
        """))

        conn.commit()

    print("Sample data inserted successfully.")


if __name__ == "__main__":
    seed_data()