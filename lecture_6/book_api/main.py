from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, dbconnect
from typing import Optional

# Create all database tables defined in models.
# Why: ensures schema is initialized before API starts.
models.Base.metadata.create_all(bind=dbconnect.engine)

# Initialize FastAPI application
app = FastAPI()

def get_db():
    """
    Dependency function to provide a database session.

    Args:
        None (FastAPI injects automatically when used with Depends).

    Returns:
        Generator yielding a SQLAlchemy Session object.

    Why:
        Ensures each request gets its own DB session and closes it after use.
    """
    db = dbconnect.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book record in the database.

    Args:
        book (schemas.BookCreate): Input data for the new book (title, author, year).
        db (Session): Database session provided by dependency.

    Returns:
        schemas.BookOut: The newly created book with its generated ID.

    Why:
        POST is used for creation. We commit and refresh to persist and return the saved object.
    """
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[schemas.BookOut], status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    """
    Retrieve all books from the database.

    Args:
        db (Session): Database session.

    Returns:
        list[schemas.BookOut]: List of all books stored.

    Why:
        GET is used for reading resources. Returns all rows without filters.
    """
    return db.query(models.Book).all()


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.

    Args:
        book_id (int): Unique identifier of the book to delete.
        db (Session): Database session.

    Returns:
        None (204 No Content).

    Why:
        DELETE removes a resource. If not found, raise 404 to indicate missing resource.
    """
    book = db.get(models.Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return


@app.put("/books/{book_id}", response_model=schemas.BookOut, status_code=status.HTTP_200_OK)
def update_book(book_id: int, new_book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Update an existing book by its ID.

    Args:
        book_id (int): Unique identifier of the book to update.
        new_book (schemas.BookCreate): New data to replace existing fields.
        db (Session): Database session.

    Returns:
        schemas.BookOut: The updated book object.

    Why:
        PUT replaces the entire resource. If not found, return 404.
    """
    book = db.get(models.Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = new_book.title
    book.author = new_book.author
    book.year = new_book.year

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search", response_model=list[schemas.BookOut], status_code=status.HTTP_200_OK)
def return_book(
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Search for books by title, author, or year.

    Args:
        title (Optional[str]): Substring to match in book titles.
        author (Optional[str]): Substring to match in author names.
        year (Optional[int]): Exact year to filter by.
        db (Session): Database session.

    Returns:
        list[schemas.BookOut]: List of books matching the filters.

    Why:
        Provides flexible search functionality. Uses ILIKE for case-insensitive matching.
        If no results, raises 404 to indicate nothing found.
    """
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(models.Book.year == year)

    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="Book not found")
    return results

@app.get ("/healthcheck")
async def heathcheck() -> dict:
    return {"status": "ok"}

