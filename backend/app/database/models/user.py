from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, Uuid
from sqlalchemy.sql.sqltypes import DateTime

from backend.app.database.session import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Uuid, primary_key=True, default=uuid4)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    avatar_path = Column(String(255), nullable=True)
    points = Column(Integer, nullable=False, default=0)
    permission = Column(String(255), nullable=False, default='user')
    created_at = Column(DateTime, nullable=True, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=datetime.now)

    def __repr__(self):
        return f'User(user_id={self.user_id}, email={self.email})'