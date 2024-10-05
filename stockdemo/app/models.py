from sqlalchemy import Column, DateTime, Float, Integer, String, func

from .database import Base


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())


class Stock(TimestampMixin, Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
