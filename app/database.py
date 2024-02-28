from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep
from .config import settings


SQLALCHEMY_DATABASE_URL = \
    f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}:{
        settings.database_port}/{settings.database_name}'
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


# Connecting Raw SQL
def connect_db_driver():
    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='fastapi',
                                    user='postgres', password='anaANA24', cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print('Database connection was successful!')
            break
        except Exception as error:
            print("Connecting to database failed")
            print("Error:", error)
            print()
            sleep(2)
