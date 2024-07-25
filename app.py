from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'], details=book['details'], short_details=book['short_details'], genre=book['genre'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(response: Response ,book_id: int, book: dict, db: Session = Depends(get_db),):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        return response.status_code == 404

@router_v1.delete('/books/{book_id}')
async def delete_book(response: Response, book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        return response.status_code == 404



@router_v1.get('/coffee')
async def get_coffee(db: Session = Depends(get_db)):
    return db.query(models.Coffee).all()

@router_v1.get('/coffee/{coffee_id}')
async def get_coffee(coffee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()

@router_v1.post('/coffee')
async def create_coffee(coffee: dict, response: Response, db: Session = Depends(get_db)):
    new_coffee = models.Coffee(name=coffee['name'], description=coffee['description'], price=coffee['price'], is_available=coffee['is_available'])
    db.add(new_coffee)
    db.commit()
    db.refresh(new_coffee)
    response.status_code = 201
    return new_coffee

@router_v1.patch('/coffee/{coffee_id}')
async def update_coffee(response: Response ,coffee_id: int, coffee: dict, db: Session = Depends(get_db),):
    db_coffee = db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()
    if db_coffee:
        for key, value in coffee.items():
            setattr(db_coffee, key, value)
        db.commit()
        db.refresh(db_coffee)
        return db_coffee
    else:
        return response.status_code == 404

@router_v1.delete('/coffee/{coffee_id}')
async def delete_coffee(response: Response, coffee_id: int, db: Session = Depends(get_db)):
    db_coffee = db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()
    if db_coffee:
        db.delete(db_coffee)
        db.commit()
        return {"message": "Coffee deleted successfully"}
    else:
        return response.status_code == 404
    
    
@router_v1.get('/orders')
async def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/orders/{order_id}')
async def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

@router_v1.post('/orders')
async def create_order(order: dict, response: Response, db: Session = Depends(get_db)):
    new_order = models.Order(coffee_id=order['coffee_id'], order_date=order['order_date'], quantity=order['quantity'], total_price=order['total_price'], notes=order['notes'])
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    response.status_code = 201
    return new_order

@router_v1.patch('/orders/{order_id}')
async def update_order(response: Response ,order_id: int, order: dict, db: Session = Depends(get_db),):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        for key, value in order.items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        return response.status_code == 404

@router_v1.delete('/orders/{order_id}')
async def delete_order(response: Response, order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return {"message": "Order deleted successfully"}
    else:
        return response.status_code == 404

# ...
app.include_router(router_v1)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
