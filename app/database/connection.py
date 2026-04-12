from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_path = os.path.abspath("data/olist.sqlite")
print("Using DB at:", db_path) 

# Create the database engine   
engine = create_engine(f"sqlite:///{db_path}")

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_engine():
    """
    Returns the SQLAlchemy engine instance.
    """
    return engine

def get_session():
    """
    Creates a new database session.
    """
    return SessionLocal()