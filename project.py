from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class BookStore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/book")
def createbook(book: BookStore, db: Session = Depends(get_db)):
    newbook = model.Book(
        id=book.id,
        title=book.title,
        author=book.author,
        publish_date=book.publish_date
    )

    db.add(newbook)
    db.commit()
    db.refresh(newbook)

    return newbook