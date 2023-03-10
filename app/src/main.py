from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .schema import schemas
from .database import models, database
from .database.database import session, engine
from .crud import crud

# DBの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"message": "Success"}

@app.get("/users", response_model=list[schemas.User])
async def users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/rooms", response_model=list[schemas.Room])
async def rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/bookings", response_model=list[schemas.Booking])
async def bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

## Create
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/rooms", response_model=schemas.Room)
async def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)

@app.post("/bookings", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)
