from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from time import sleep
from .config import settings


SQLALCHEMY_DATABASE_URL = "postgres://bebo:YfEzm6rG60JZVREXj3EnCDbuayu0uMsr@dpg-con9inocmk4c73a1g1u0-a.oregon-postgres.render.com/bebo"
# '<DBMS-name>://<username>:<password>@<ip-address/hostname>:<port>/<database-name>'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
