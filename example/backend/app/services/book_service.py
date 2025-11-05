from example.backend.app.api.v1.exceptions.empty_name_exception import EmptyNameException
from example.backend.app.repositories.book_repository import BookRepository
from sqlalchemy.ext.asyncio import AsyncSession


class BookService:
    def __init__(self, session: AsyncSession):
        self.repo = BookRepository(session)

    async def get_books(self):
        return await self.repo.get_all()

    async def create_book(self, title: str):
        if len(title) == 0:
            raise EmptyNameException()
        return await self.repo.create(title)
