from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Addresses(Base):
    __tablename__ = 'addresses'

    address_id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    street_address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(20))

    persons = relationship("Association", back_populates="address")
