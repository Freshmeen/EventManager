from uuid import UUID
from typing import List

from backend.app.api.v1.exceptions.event_members import (
    EventMemberNotFoundException,
    EventMemberAlreadyExistsException
)
from backend.app.api.v1.models.event_member import EventMemberCreate, EventMemberUpdate
from backend.app.database.models import EventMember
from backend.app.repositories.event_member_repository import EventMemberRepository
from backend.app.services.data.EventAcceptationStatus import EventAcceptationStatus


class EventMemberService:
    def __init__(self, repo: EventMemberRepository):
        self._repo = repo

    async def get_member(self, event_id: UUID, user_id: UUID) -> EventMember:
        member = await self._repo.get_by_ids(event_id, user_id)
        if member is None:
            raise EventMemberNotFoundException(user_id=user_id, event_id=event_id)
        return member

    async def get_members_by_event(self, event_id: UUID) -> List[EventMember]:
        return await self._repo.get_by_event(event_id)

    async def get_memberships_by_user(self, user_id: UUID) -> List[EventMember]:
        return await self._repo.get_by_user(user_id)

    async def add_member(self, member_in: EventMemberCreate) -> EventMember:
        existing = await self._repo.get_by_ids(member_in.event_id, member_in.user_id)
        if existing:
            raise EventMemberAlreadyExistsException(
                user_id=member_in.user_id,
                event_id=member_in.event_id
            )

        member = EventMember(
            user_id=member_in.user_id,
            event_id=member_in.event_id,
            role=member_in.role,
            comment=member_in.comment,
            acceptation_status=EventAcceptationStatus.PENDING.value
        )
        return await self._repo.create(member)

    async def update_member(self, event_id: UUID, user_id: UUID, update_in: EventMemberUpdate):
        member = await self.get_member(event_id, user_id)

        update_data = update_in.model_dump(exclude_unset=True)

        if "acceptation_status" in update_data and update_data["acceptation_status"]:
            update_data["acceptation_status"] = update_data["acceptation_status"].value

        for k, v in update_data.items():
            setattr(member, k, v)

        return None

    async def remove_member(self, event_id: UUID, user_id: UUID):
        await self.get_member(event_id, user_id)
        await self._repo.delete(event_id, user_id)