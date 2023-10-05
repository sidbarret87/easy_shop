from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


Base = declarative_base()

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class Product(Base):
    __tablename__= 'products'
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric(10,2))
    created_at = Column(TIMESTAMP, nullable=False,  default=func.now())


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_email = Column(String)
    total_cost = Column(Numeric(10,2))
    created_at = Column(TIMESTAMP)
