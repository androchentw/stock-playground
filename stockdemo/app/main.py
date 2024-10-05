from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/stocks/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    return crud.create_stock(db=db, stock=stock)


@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock
