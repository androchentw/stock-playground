from pydantic import BaseModel


class StockBase(BaseModel):
    name: str
    price: float


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    id: int

    class Config:
        # allow database schemas mapping to ORM objects
        orm_mode = True
