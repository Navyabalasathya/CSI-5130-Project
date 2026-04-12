from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


def build_vector_store():

    docs = [

        # 🧑 Customers
        Document(page_content="""
        Table: customers
        Columns: customer_id, customer_city, customer_state
        Description: Stores customer information and location
        Use: customer-based queries, filtering by city/state
        Relation: customers.customer_id = orders.customer_id
        """),

        # 📦 Orders
        Document(page_content="""
        Table: orders
        Columns: order_id, customer_id, order_status, order_purchase_timestamp
        Description: Contains order lifecycle and timestamps
        Use: order history, time-based queries
        Relation: orders.customer_id = customers.customer_id
        Relation: orders.order_id = order_items.order_id
        Relation: orders.order_id = order_payments.order_id
        Relation: orders.order_id = order_reviews.order_id
        """),

        # 🛒 Order Items
        Document(page_content="""
        Table: order_items
        Columns: order_id, product_id, seller_id, price, freight_value
        Description: Items within each order
        Use: revenue calculation, product sales
        Relation: order_items.order_id = orders.order_id
        Relation: order_items.product_id = products.product_id
        Relation: order_items.seller_id = sellers.seller_id
        """),

        # 💳 Payments
        Document(page_content="""
        Table: order_payments
        Columns: order_id, payment_type, payment_value
        Description: Payment details for orders
        Use: total revenue, payment analysis
        Relation: order_payments.order_id = orders.order_id
        """),

        # ⭐ Reviews
        Document(page_content="""
        Table: order_reviews
        Columns: order_id, review_score
        Description: Customer reviews for orders
        Use: satisfaction analysis, average ratings
        Relation: order_reviews.order_id = orders.order_id
        """),

        # 🛍 Products
        Document(page_content="""
        Table: products
        Columns: product_id, product_category_name
        Description: Product details and category
        Use: product analysis, category-based queries
        Relation: products.product_id = order_items.product_id
        """),

        # 🏪 Sellers
        Document(page_content="""
        Table: sellers
        Columns: seller_id, seller_city, seller_state
        Description: Seller information
        Use: seller performance, regional analysis
        Relation: sellers.seller_id = order_items.seller_id
        """),

        # 🌍 Geolocation (optional but useful)
        Document(page_content="""
        Table: geolocation
        Columns: geolocation_zip_code_prefix, geolocation_city, geolocation_state
        Description: Maps zip codes to location
        Use: geographic analysis
        """),

        # 🌐 Category Translation
        Document(page_content="""
        Table: product_category_name_translation
        Columns: product_category_name, product_category_name_english
        Description: Translates category names to English
        Use: better readability of product categories
        """),

        # 🔥 EXAMPLES (VERY IMPORTANT)

        Document(page_content="""
        Question: Top 5 customers by total spending
        SQL:
        SELECT c.customer_id, SUM(p.payment_value) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_payments p ON o.order_id = p.order_id
        GROUP BY c.customer_id
        ORDER BY total_spent DESC
        LIMIT 5;
        """),

        Document(page_content="""
        Question: Top selling product categories
        SQL:
        SELECT pr.product_category_name, COUNT(*) AS total_sales
        FROM order_items oi
        JOIN products pr ON oi.product_id = pr.product_id
        GROUP BY pr.product_category_name
        ORDER BY total_sales DESC
        LIMIT 5;
        """),

        Document(page_content="""
        Question: Average review score
        SQL:
        SELECT AVG(review_score) FROM order_reviews;
        """),
        
        Document(page_content="""
        Common Join Patterns:

        customers → orders → order_payments (for revenue)
        orders → order_items → products (for product analysis)
        orders → order_reviews (for ratings)

        Always use proper JOIN conditions.
        """)
    ]

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    #OpenAIEmbeddings(model="text-embedding-3-small")
    vector_db = FAISS.from_documents(docs, embeddings)

    return vector_db


# 🔹 Retrieve relevant context
def get_relevant_context(question: str, db, k: int = 3):
    docs = db.similarity_search(question, k=k)
    return "\n".join([doc.page_content for doc in docs])