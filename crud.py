from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app=FastAPI()
books = [
    {
        "id": 1,
        "title": "Dekho Na",
        "author": "James Bond",
        "publish_date": "19-03-2017"
    },
    {
        "id": 2,
        "title": "The Silent Code",
        "author": "R.K. Sharma",
        "publish_date": "11-07-2019"
    },
    {
        "id": 3,
        "title": "FastAPI Mastery",
        "author": "Mohit Tiwari",
        "publish_date": "01-01-2025"
    },
    {
        "id": 4,
        "title": "Python Deep Dive",
        "author": "Guido Rossum",
        "publish_date": "15-08-2015"
    },
    {
        "id": 5,
        "title": "Async World",
        "author": "Andrew Ng",
        "publish_date": "22-02-2022"
    }
]

@app.get("/books")
def get_book():
    return books

@app.get("/getbook/{id}")
def getbook(id:int):
    for book in books:
        if(book["id"]==id):
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#post method for creat new data or add data in server 
class edit_book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str
@app.post("/editbook")
def edit(book:edit_book):
    newbook=book.model_dump()
    books.append(newbook)
    
    return books
#updatebook
class bookupdate(BaseModel):
    title:str
    author:str
    publish_date:str
@app.put("/updatebook/{id}")
def updatebook(id: int, book_update: bookupdate):
    for book in books:
        if book["id"] == id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publish_date"] = book_update.publish_date
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

#delete
@app.delete("/delbook/{id}")
def deletebook(id:int):
    for book in books:
        if book["id"]==id:
            books.remove(book)
            return {"message":"our book is delete"}
            

