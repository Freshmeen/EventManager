from uuid import uuid4

from sqlalchemy import Column, Integer, String, Uuid

from backend.app.database.base import LifecycleMixin, UpdatedAtMixin
from backend.app.database.models.data import UserPermissionType
from backend.app.database.session import Base


class User(LifecycleMixin, UpdatedAtMixin, Base):
    __tablename__ = 'user'

    user_id = Column(Uuid, primary_key=True, default=uuid4)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    avatar_path = Column(String(255), nullable=True)
    points = Column(Integer, nullable=False, default=0)
    permission = Column(UserPermissionType(), nullable=False, default='user')

    def __repr__(self):
        return f'User(user_id={self.user_id}, email={self.email}, permission={self.permission})'
