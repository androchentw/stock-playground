from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from loguru import logger
from .database import engine, get_db
from . import crud, models, schemas


def get_app() -> FastAPI:
    """Instanciating and setting up FastAPI application."""
    api_app = FastAPI()

    origins = [
        "http://localhost:5050",
    ]
    api_app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # api_app.include_router(api_router, prefix=settings.api_prefix)

    return api_app


app = get_app()
models.Base.metadata.create_all(bind=engine)


# ===== App Info Endpoints ===== #
@app.get("/")
async def root():
    return {"message": "OK"}


@app.get("/logger_test")
async def test_logger():
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
    return {"message": "Check log types produced by app"}


@app.post("/stocks", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    return crud.create_stock(db=db, stock=stock)


@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock
