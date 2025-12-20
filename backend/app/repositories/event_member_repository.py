from typing import Optional, List
from uuid import UUID

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import EventMember
from backend.app.repositories.base import BaseRepository


class EventMemberRepository(BaseRepository[EventMember]):
    def __init__(self, session: AsyncSession):
        super().__init__(EventMember, session)

    async def get_by_ids(self, event_id: UUID, user_id: UUID) -> Optional[EventMember]:
        result = await self.session.execute(
            select(EventMember).where(
                and_(
                    EventMember.event_id == event_id,
                    EventMember.user_id == user_id,
                    EventMember.deleted_at.is_(None)
                )
            )
        )
        return result.scalar_one_or_none()

    async def get_by_event(self, event_id: UUID) -> List[EventMember]:
        result = await self.session.execute(
            select(EventMember).where(
                EventMember.event_id == event_id,
                EventMember.deleted_at.is_(None)
            )
        )
        return list(result.scalars().all())

    async def get_by_user(self, user_id: UUID) -> List[EventMember]:
        result = await self.session.execute(
            select(EventMember).where(
                EventMember.user_id == user_id,
                EventMember.deleted_at.is_(None)
            )
        )
        return list(result.scalars().all())

    async def create(self, member: EventMember) -> EventMember:
        self.session.add(member)
        await self.session.flush()
        await self.session.refresh(member)
        return member

    async def delete(self, event_id: UUID, user_id: UUID):
        member = await self.get_by_ids(event_id, user_id)
        if member:
            member.soft_delete()
            await self.session.flush()