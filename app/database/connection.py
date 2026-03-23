from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///data/sample_database.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

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