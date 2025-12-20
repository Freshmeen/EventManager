from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.v1.models.event_member import (
    EventMemberCreate,
    EventMemberResponse,
    EventMemberUpdate
)
from backend.app.database.session import get_db
from backend.app.repositories.event_member_repository import EventMemberRepository
from backend.app.services.event_member_service import EventMemberService

router = APIRouter(prefix="/event-members", tags=["event-members"])


def get_event_member_service(session: AsyncSession = Depends(get_db)) -> EventMemberService:
    repo = EventMemberRepository(session)
    return EventMemberService(repo)


@router.post(
    "/",
    response_model=EventMemberResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a user to an event"
)
async def add_member(
    member_in: EventMemberCreate,
    service: EventMemberService = Depends(get_event_member_service)
):
    return await service.add_member(member_in)


@router.get(
    "/event/{event_id}",
    response_model=List[EventMemberResponse],
    summary="List all members of an event"
)
async def list_event_members(
    event_id: UUID,
    service: EventMemberService = Depends(get_event_member_service)
):
    return await service.get_members_by_event(event_id)


@router.get(
    "/user/{user_id}",
    response_model=List[EventMemberResponse],
    summary="List all events a user is member of"
)
async def list_user_memberships(
    user_id: UUID,
    service: EventMemberService = Depends(get_event_member_service)
):
    return await service.get_memberships_by_user(user_id)


@router.get(
    "/{event_id}/{user_id}",
    response_model=EventMemberResponse,
    summary="Get specific membership details"
)
async def get_membership(
    event_id: UUID,
    user_id: UUID,
    service: EventMemberService = Depends(get_event_member_service)
):
    return await service.get_member(event_id, user_id)


@router.patch(
    "/{event_id}/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update membership (role, status, comment)"
)
async def update_membership(
    event_id: UUID,
    user_id: UUID,
    update_in: EventMemberUpdate,
    service: EventMemberService = Depends(get_event_member_service)
):
    await service.update_member(event_id, user_id, update_in)


@router.delete(
    "/{event_id}/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove user from event"
)
async def remove_member(
    event_id: UUID,
    user_id: UUID,
    service: EventMemberService = Depends(get_event_member_service)
):
    await service.remove_member(event_id, user_id)