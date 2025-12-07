from backend.app.database.base import UpdatedAtMixin, LifecycleMixin
from backend.app.database.models.data import AcceptationStatus
from backend.app.database.session import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Uuid, String, DateTime, Integer
from uuid import uuid4


class Event(LifecycleMixin, UpdatedAtMixin, Base):
    __tablename__ = "event"
    event_id = Column(Uuid, primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    acceptation_status = Column(String(255), nullable=False, default=AcceptationStatus.PENDING)
    starts_at = Column(DateTime, nullable=False)
    ends_at = Column(DateTime, nullable=False)
    min_volunteers = Column(Integer, nullable=True)
    max_volunteers = Column(Integer, nullable=True)
    image_path = Column(String(255), nullable=True)
