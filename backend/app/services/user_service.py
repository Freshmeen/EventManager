from typing import Optional, List
from uuid import UUID

from backend.app.api.v1.exceptions.EmailAlreadyRegisteredException import EmailAlreadyExistsException
from backend.app.api.v1.models.user import UserCreate, UserUpdate
from backend.app.repositories.user_repository import UserRepository
from backend.app.database.models.user import User
import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))

class UserService:
    def __init__(self, user_repo: UserRepository):
        self._repo = user_repo

    async def get_by_id(self, user_id: UUID) -> Optional[User]:
        return await self._repo.get_by_id(user_id)

    async def get_by_email(self, email: str) -> Optional[User]:
        return await self._repo.get_by_email(email)

    async def list_all(self) -> List[User]:
        return await self._repo.get_all()

    async def create(self, user_create: UserCreate) -> UUID:  # передаём схему
        if await self._repo.get_by_email(str(user_create.email)):
            raise EmailAlreadyExistsException(str(user_create.email))
        user = User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            middle_name=user_create.middle_name,
            email=str(user_create.email),
            password_hash=hash_password(user_create.password),
            avatar_path=user_create.avatar_path,
            permission=user_create.permission,
        )
        user_id = await self._repo.create(user)
        return user_id

    async def update(self, user_id: UUID, user_update: UserUpdate) -> Optional[User]:
        update_data = user_update.model_dump(exclude_unset=True)
        if not update_data:
            return await self._repo.get_by_id(user_id)
        return await self._repo.update(user_id, **update_data)

    async def delete(self, user_id: UUID):
        await self._repo.delete(user_id)

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        user = await self._repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            return None
        return user