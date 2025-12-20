from uuid import UUID
from pydantic import BaseModel
from backend.app.services.data.EventAcceptationStatus import EventAcceptationStatus


class EventMemberBase(BaseModel):
    role: str = "volunteer"
    comment: str | None = None


class EventMemberCreate(EventMemberBase):
    user_id: UUID
    event_id: UUID


class EventMemberUpdate(BaseModel):
    role: str | None = None
    acceptation_status: EventAcceptationStatus | None = None
    comment: str | None = None


class EventMemberResponse(EventMemberBase):
    user_id: UUID
    event_id: UUID
    acceptation_status: str

    model_config = {
        "from_attributes": True,
    }