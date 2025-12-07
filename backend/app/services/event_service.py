from datetime import datetime, timezone
from uuid import UUID

from backend.app.api.v1.exceptions.events import EventNotFoundException
from backend.app.api.v1.models.event import EventCreate, EventUpdate
from backend.app.database.models import Event
from backend.app.repositories.event_repository import EventRepository
from backend.app.services.data.EventAcceptationStatus import EventAcceptationStatus


class EventService:
    def __init__(self, event_repo: EventRepository):
        self._repo = event_repo

    async def get_by_id(self, event_id: UUID) -> Event:
        event = await self._repo.get_by_id(event_id)
        if event is None:
            raise EventNotFoundException(event_id=event_id)
        return event

    async def get_future(self):
        events = await self._repo.get_by_time_interval(since=datetime.now(timezone.utc))
        return events

    async def get_past(self):
        events = await self._repo.get_by_time_interval(until=datetime.now(timezone.utc))
        return events

    async def list_all(self):
        return await self._repo.get_all()

    async def create(self, event_create: EventCreate,
                     status: EventAcceptationStatus = EventAcceptationStatus.ACCEPTED) -> UUID:
        event = Event(
            name=event_create.name,
            description=event_create.description,
            acceptation_status=status,
            starts_at=event_create.starts_at,
            ends_at=event_create.ends_at,
            min_volunteers=event_create.min_volunteers,
            max_volunteers=event_create.max_volunteers,
            image_path=event_create.image_path,
        )
        event_id = await self._repo.create(event)
        return event_id

    async def suggest(self, event_create: EventCreate) -> UUID:
        return await self.create(event_create, EventAcceptationStatus.PENDING)

    async def reject(self, event_id: UUID):
        event = await self.get_by_id(event_id)
        event.acceptation_status = EventAcceptationStatus.REJECTED

    async def accept(self, event_id: UUID):
        event = await self.get_by_id(event_id)
        event.acceptation_status = EventAcceptationStatus.ACCEPTED

    async def update(self, event_id: UUID, user_update: EventUpdate):
        user = await self._repo.get_by_id(event_id)

        update_data = user_update.model_dump(exclude_unset=True)

        for k, v in update_data.items():
            setattr(user, k, v)

        return None

    async def delete(self, event_id: UUID):
        await self._repo.delete(event_id)
