from fastapi import FastAPI, HTTPException, Body

app = FastAPI(title="Simple Bookstore API")

# In-memory data
books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

# Auto-increment ID
def get_next_id():
    return max([book["id"] for book in books], default=0) + 1

# GET all books
@app.get("/books")
def get_books():
    return books

# GET book by ID (used before updating)
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# POST add book
@app.post("/books")
def add_book(
    book: dict = Body(
        ...,
        example={
            "title": "",
            "author": ""
        }
    )
):
    new_book = {
        "id": get_next_id(),
        "title": book["title"],
        "author": book["author"]
    }
    books.append(new_book)
    return new_book

# PUT update book
@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    data: dict = Body(
        ...,
        example={
            "title": "",
            "author": ""
        }
    )
):
    for book in books:
        if book["id"] == book_id:
            book["title"] = data["title"]
            book["author"] = data["author"]
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
