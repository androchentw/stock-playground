from pydantic import BaseModel


class StockBase(BaseModel):
    name: str
    price: float


class StockCreate(StockBase):
    pass


class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True
