from enum import IntEnum


class UserPermission(IntEnum):
    ADMIN = 0b1
    EVENT_CREATOR = 0b10

    def __repr__(self):
        return self.name
