from fastapi import FastAPI

from app.database import engine, Base

# Import models
from app.models.book import Book
from app.models.member import Member
from app.models.borrow_record import BorrowRecord

# Import routers
from app.routers import book, member, borrow_record


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Library Management System",
    description="API for managing books, members, and borrow/return transactions",
    version="1.0.0"
)


# Register routers
app.include_router(book.router)
app.include_router(member.router)
app.include_router(borrow_record.router)


@app.get("/")
def root():
    return {
        "message": "Library Management System API is running"
    }