from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, and_

from backend.app.database.models import Event
from backend.app.repositories.base import BaseRepository


class EventRepository(BaseRepository[Event]):
    def __init__(self, session: AsyncSession):
        super().__init__(Event, session)

    async def get_by_id(self, event_id: UUID) -> Optional[Event]:
        result = await self.session.execute(select(Event).where(Event.event_id == event_id, Event.deleted_at.is_(None)))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[Event]:
        result = await self.session.execute(select(Event))
        return list(result.scalars().all())

    async def create(self, event: Event) -> UUID:
        self.session.add(event)
        await self.session.flush()
        await self.session.refresh(event)
        return event.event_id

    async def delete(self, event_id: UUID):
        event = await self.get_by_id(event_id)
        event.soft_delete()
        await self.session.flush()

    async def list_by_time_interval(self, since: datetime = None, until: datetime = None):
        stmt = select(Event)

        conditions = []
        if since:
            conditions.append(Event.ends_at >= since)
        if until:
            conditions.append(Event.starts_at <= until)

        if conditions:
            stmt = stmt.where(and_(*conditions))

        result = await self.session.execute(stmt)
        return result.scalars().all()
