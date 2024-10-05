import datetime

from pydantic import BaseModel


class StockBase(BaseModel):
    name: str
    price: float
    description: str | None = None


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        # allow database schemas mapping to ORM objects
        orm_mode = True
