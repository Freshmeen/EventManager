from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.v1.models.event import EventCreateResponse, EventCreate, EventResponse, EventUpdate
from backend.app.database.session import get_db
from backend.app.repositories.event_repository import EventRepository
from backend.app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])


def get_event_service(session: AsyncSession = Depends(get_db)) -> EventService:
    repo = EventRepository(session)
    return EventService(repo)


@router.post(
    "/",
    response_model=EventCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new event"
)
async def create_event(
        event_in: EventCreate,
        service: EventService = Depends(get_event_service),
):
    event_id = await service.create(event_in)
    return EventCreateResponse(event_id=event_id)


@router.post(
    "/suggest",
    response_model=EventCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Suggest a new event"
)
async def suggest_event(
        event_in: EventCreate,
        service: EventService = Depends(get_event_service),
):
    event_id = await service.suggest(event_in)
    return EventCreateResponse(event_id=event_id)


@router.get(
    "/{event_id}",
    response_model=EventResponse,
    summary="Get event by ID",
    response_model_exclude_none=True,
)
async def get_event(
        event_id: UUID,
        service: EventService = Depends(get_event_service),
):
    return await service.get_by_id(event_id)


@router.patch(
    "/{event_id}/accept",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Accept an event",
)
async def accept_event(
        event_id: UUID,
        service: EventService = Depends(get_event_service),
):
    await service.accept(event_id)


@router.patch(
    "/{event_id}/reject",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Accept an event",
)
async def reject_event(
        event_id: UUID,
        service: EventService = Depends(get_event_service),
):
    await service.reject(event_id)


@router.get(
    "/",
    response_model=list[EventResponse],
    summary="List all events",
    response_model_exclude_none=True,
)
async def list_events(service: EventService = Depends(get_event_service)):
    return await service.list_all()


@router.patch(
    "/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update event partially",
)
async def update_event(
        event_id: UUID,
        event_update: EventUpdate,
        service: EventService = Depends(get_event_service)
):
    await service.update(event_id, event_update)


@router.delete(
    "/{event_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete event"
)
async def delete_event(
        event_id: UUID,
        service: EventService = Depends(get_event_service)
):
    await service.delete(event_id)
