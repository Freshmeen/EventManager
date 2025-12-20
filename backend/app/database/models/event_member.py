from sqlalchemy import Column, String, ForeignKey, Text, Uuid
from sqlalchemy.orm import relationship

from backend.app.database.base import LifecycleMixin
from backend.app.database.models.data import AcceptationStatus
from backend.app.database.session import Base


class EventMember(LifecycleMixin, Base):
    __tablename__ = "event_member"

    user_id = Column(Uuid, ForeignKey("user.user_id"), primary_key=True)
    event_id = Column(Uuid, ForeignKey("event.event_id"), primary_key=True)

    role = Column(String(50), nullable=False, default="volunteer")
    acceptation_status = Column(String(255), nullable=False, default=AcceptationStatus.PENDING.value)
    comment = Column(Text, nullable=True)

    user = relationship("User", backref="event_memberships", lazy="selectin")
    event = relationship("Event", backref="user_memberships", lazy="selectin")