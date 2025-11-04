from fastapi import APIRouter, Depends
from example.backend.app.api.v1.models.book import BookCreate, BookRead
from example.backend.app.database.session import get_db
from example.backend.app.services.book_service import BookService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookRead], operation_id="get_books")
async def get_books(db: AsyncSession = Depends(get_db)):
    return await BookService(db).get_books()

@router.post("/", response_model=BookRead, operation_id="create_book")
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await BookService(db).create_book(book.title)
