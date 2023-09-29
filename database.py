from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db.db")
Session = sessionmaker(autocommit=False, bind=engine)
session = Session()
Base = declarative_base()
meta = MetaData()
