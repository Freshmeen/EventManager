from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

class BaseRepository[T: DeclarativeBase]:
    def __init__(self, model: type[T], session: AsyncSession):
        self.model = model
        self.session = session