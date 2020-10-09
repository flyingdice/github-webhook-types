"""
    ghwht/events/create
    ~~~~~~~~~~~~~~~~~~~

    Contains types for the 'create' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#create
"""
import enum
from typing import Optional

from pydantic import dataclasses

from . import base, common


class RefType(str, enum.Enum):
    Branch = 'branch'
    Tag = 'tag'


class PusherType(str, enum.Enum):
    User = 'user'


@dataclasses.dataclass
class Payload(base.Payload):
    description: Optional[str]
    master_branch: str
    pusher_type: PusherType
    ref: str
    ref_type: RefType
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Action = base.Action
Name = base.EventName.Create
ID = base.ID[Action]
Event = base.Event[ID, Payload]
