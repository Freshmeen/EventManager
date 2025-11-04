from sqlalchemy import select
from example.backend.app.repositories.base import BaseRepository
from example.backend.app.database.models import Book


class BookRepository(BaseRepository):

    async def get_all(self):
        result = await self.session.execute(select(Book))
        return result.scalars().all()

    async def create(self, title: str):
        book = Book(title=title)
        self.session.add(book)
        await self.session.commit()
        await self.session.refresh(book)
        return book
