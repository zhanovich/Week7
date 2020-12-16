from connection import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'people_master'

    person_id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    person_name = Column(String(255))
    person_DOB = Column(Date)
    active_phone_number = Column(String(20))

    addresses = relationship("Association", back_populates="person")
