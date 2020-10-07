"""
    ghwht/hooks/base
    ~~~~~~~~~~~~~~~~

    Contains types generic to all GitHub webhooks.
"""
import abc
import enum

from typing import ClassVar, Generic, Optional, TypeVar
from uuid import UUID

from pydantic import dataclasses, generics

from . import common


class EventName(enum.Enum):
    """
    Enumeration for all known GitHub webhook events.
    """
    Installation = 'installation'
    Ping = 'ping'


class Action(enum.Enum):
    """
    Represents a Github event action.

    This is a marker class so we can apply inheritance constraints on generic
    types and can never implement actual enumeration values. Abstract in the strictest sense.
    """


# Generic type var for types derived from :class:`~ghwht.hooks.base.Action`.
AT = TypeVar('AT', bound=Action)


class Payload(metaclass=abc.ABCMeta):
    """
    Represents a Github event payload.

    This is a marker class so we can apply inheritance constraints on generic
    types and shouldn't implement any fields. Abstract in the strictest sense.
    """


@dataclasses.dataclass
class EmptyPayload(Payload):
    """
    Represents an empty Github event payload.
    """


@dataclasses.dataclass
class StandardPayload(Payload):
    """
    Represents a standard Github event payload.

    This contains commonly found information about the context that generated the webhook event.
    """
    installation: Optional[common.Installation]
    organization: Optional[common.Organization]
    repository: Optional[common.Repository]
    sender: Optional[common.Sender]


# Generic type var for types derived from :class:`~ghwht.hooks.base.Payload`.
PT = TypeVar('PT', bound=Payload)


class Event(generics.GenericModel, Generic[AT, PT]):
    """
    Represents an abstract Github webhook event.

    All known GitHub webhook events should derive from this class and define the
    event 'name' that they should be parsed from.

    Event models encapsulate information that comes in both the webhook request payload
    and HTTP headers.
    """
    name: ClassVar[EventName]

    delivery_id: UUID
    hook_id: int
    action: Optional[AT]
    payload: PT

    @property
    def installation_id(self):
        return getattr(getattr(self.payload, 'installation', None), 'id', None)

    class Config:
        arbitrary_types_allowed = True
