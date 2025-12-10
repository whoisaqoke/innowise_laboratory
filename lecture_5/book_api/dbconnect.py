from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL.

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the database engine.

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory bound to the engine.

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Define the base class for all ORM models.

Base = declarative_base()
