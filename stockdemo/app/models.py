from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    price = Column(Float, nullable=False)
