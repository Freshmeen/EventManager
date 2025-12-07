from backend.app.api.v1.exceptions.base import NotFoundException
from uuid import UUID

class EventNotFoundException(NotFoundException):
    def __init__(self, *, event_id: UUID = None):
        super().__init__(f"Event {event_id} is not found", "EVENT_NOT_FOUND")
