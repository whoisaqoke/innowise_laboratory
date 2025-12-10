from pydantic import BaseModel
from typing import Optional

# Schema for creating a new book
class BookCreate(BaseModel):
    # Title of the book (required)
    title: str
    # Author of the book (required)
    author: str
    # Year of publication (optional, can be omitted)
    year: Optional[int] = None


# Schema for returning a book (output model)

class BookOut(BookCreate):
    # Unique identifier of the book (assigned by the database)
    id: int

    class Config:
        # Enable ORM mode so Pydantic can read data directly from SQLAlchemy models
        orm_mode = True
