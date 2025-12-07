from datetime import datetime
from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from backend.app.database.models import User
from backend.app.repositories.base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_id(self, user_id: UUID) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.user_id == user_id, User.deleted_at.is_(None)))
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        result = await self.session.execute(select(User).where(User.deleted_at.is_(None)))
        return list(result.scalars().all())

    async def create(self, user: User) -> UUID:
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user.user_id

    async def delete(self, user_id: UUID):
        user = await self.get_by_id(user_id)
        user.soft_delete()
        await self.session.flush()