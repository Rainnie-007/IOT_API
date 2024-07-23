from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

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

