# app/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from core.config import settings

# Example:
# postgresql://user:password@localhost:5432/mydb
DATABASE_URL = "postgresql://postgres:password@localhost:5432/fastapi_db"

# Engine (Production Config)
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # number of connections to keep
    max_overflow=20,       # extra connections if needed
    pool_pre_ping=True,    # checks connection health
    echo=False             # set True for debugging SQL queries
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()


# Dependency (VERY IMPORTANT)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()