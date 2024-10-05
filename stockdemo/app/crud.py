from sqlalchemy.orm import Session
from . import models, schemas


def get_stock(db: Session, stock_id: int):
    return db.query(models.Stock).filter(models.Stock.id == stock_id).first()


def create_stock(db: Session, stock: schemas.StockCreate):
    db_stock = models.Stock(name=stock.name, price=stock.price)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock
