from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, conint, field_validator, ValidationInfo


class VolunteersValidation:
    # noinspection PyNestedDecorators
    @field_validator("max_volunteers", mode='after')
    @classmethod
    def check_min_max_volunteers(cls, max_volunteers, info: ValidationInfo):
        min_volunteers = info.data.get("min_volunteers")

        if isinstance(min_volunteers, int) and isinstance(min_volunteers, int) and min_volunteers > max_volunteers:
            raise ValueError("max_volunteers must be greater than min_volunteers")

        return max_volunteers


class EventIntervalValidation:
    # noinspection PyNestedDecorators
    @field_validator("ends_at", mode='after')
    @classmethod
    def check_start_end(cls, ends_at: datetime, info: ValidationInfo):
        starts_at = info.data.get("starts_at")

        if isinstance(starts_at, datetime) and isinstance(ends_at, datetime) and starts_at > ends_at:
            raise ValueError("ends_at must be greater than starts_at")

        return ends_at


class EventBase(VolunteersValidation, EventIntervalValidation, BaseModel):
    name: str
    description: str | None = None
    starts_at: datetime
    ends_at: datetime
    min_volunteers: conint(ge=0) | None = None
    max_volunteers: conint(ge=0) | None = None
    image_path: str | None = None


class EventCreate(EventBase):
    pass


class EventUpdate(VolunteersValidation, EventIntervalValidation, BaseModel):
    name: str | None = None
    description: str | None = None
    starts_at: datetime | None = None
    ends_at: datetime | None = None
    min_volunteers: conint(ge=0) | None = None
    max_volunteers: conint(ge=0) | None = None
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
