from enum import IntEnum


class UserPermission(IntEnum):
    ADMIN = 0b1
    EVENT_PARTICIPANT = 0b10
    EVENT_CREATOR = 0b100

    def __repr__(self):
        return self.name
