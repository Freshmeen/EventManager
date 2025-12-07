from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    description: str | None = None
    starts_at: datetime
    ends_at: datetime
    min_volunteers: int | None = None
    max_volunteers: int | None = None
    image_path: str | None = None


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    min_volunteers: int | None = None
    max_volunteers: int | None = None
    image_path: str | None = None


class EventCreateResponse(BaseModel):
    event_id: UUID

    model_config = {
        "from_attributes": True,
    }


class EventResponse(EventBase):
    event_id: UUID

    model_config = {
        "from_attributes": True,
    }