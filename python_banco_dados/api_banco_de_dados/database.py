from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:pg_vago@127.0.0.1:5433/escola"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, pool_timeout=5000)
SessionLocal = sessionmaker(bind=engine)
print("DATABASE_URL")
Base = declarative_base()
