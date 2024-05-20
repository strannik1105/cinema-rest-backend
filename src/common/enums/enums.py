from enum import Enum, StrEnum, auto


class Role(StrEnum):
    SUPERUSER = auto()
    ADMIN = auto()
    MEMBER = auto()


class EventRole(StrEnum):
    ORGANIZER = auto()
    MEMBER = auto()
