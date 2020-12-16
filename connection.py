from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost:3306/AddressBookAlchemy')
Base = declarative_base()
session = sessionmaker(bind=engine)()
