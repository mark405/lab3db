from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import DB_URL

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
