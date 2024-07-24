from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy import DateTime

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    details = Column(String, index=True)
    short_details = Column(String, index=True)
    genre = Column(String, index=True)

class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    is_available = Column(Boolean, index=True)
    
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    order_date = Column(DateTime, index=True)
    quantity = Column(Integer, index=True)
    total_price = Column(Integer, index=True)
    notes = Column(String, index=True)




