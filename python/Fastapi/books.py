from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for input validation
class Book(BaseModel):
    id: int
    author_id: str
    title: str
def __init__(self, id, author_id, title):
        self.id = id
        self.author_id = author_id
        self.title = title
Books = [
    Book(id=1, author_id="1", title="Book 1"),
    Book(id=2, author_id="2", title="Book 2"),
    Book(id=3, author_id="3", title="Book 3") 
]

# GET all books
@app.get("/books")
async def get_books():
    return Books

# GET book by title (query parameter)
@app.get("/books/")
async def get_book_by_title(title: str):
    for book in Books:
        if book["title"].lower() == title.lower():
            return book
    return {"message": "Book not found"}

# POST - Create a new book
@app.post("/create")
async def create_book(new_book: Book):
    book = new_book.dict()
    book["id"] = len(Books) + 1
    Books.append(book)
    return book

# PUT - Update an existing book
@app.put("/update/{id}")
async def update_book(id: int, updated_book: Book):
    for book in Books:
        if book["id"] == id:
            book.update(updated_book.dict())
            return book
    return {"message": "Book not found"}

# DELETE - Delete a book
@app.delete("/delete/{id}")
async def delete_book(id: int):
    for book in Books:
        if book["id"] == id:
            Books.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}