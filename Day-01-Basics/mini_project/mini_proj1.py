from fastapi import FastAPI,Query,HTTPException
from pydantic import BaseModel,Field
app=FastAPI()

class Book(BaseModel):
    title: str=Field(...,min_length=1)
    author: str=Field(...,min_length=3)
    pages: int=Field(...,gt=10)

books={
    1:{"title":"Dad Book",
        "author":"Ramesh",
        "pages":300},
    2:{"title":"Mom Book",
        "author":"Saritha",
        "pages":200},
    3:{"title":"Sister Book",
        "author":"Harshitha",
        "pages":100},
    }

@app.get("/books")

def library():
    return books

@app.get("/books/{book_id}")

def book_id(book_id:int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found!")
    return books[book_id]

@app.post("/add-book")

def add_book(book_id: int, new_book:Book):
    if book_id in books:
        raise HTTPException(status_code=400, detail="This ID already exists!")
    
    books[book_id] = new_book.model_dump() # model_dump is a dictioney
    return {"message":"Book added successfully", "book": books[book_id]}