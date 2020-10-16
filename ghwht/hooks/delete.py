"""
    ghwht/events/delete
    ~~~~~~~~~~~~~~~~~~~

    Contains types for the 'delete' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#delete
"""
import enum
from typing import Optional

from pydantic import dataclasses

from . import base, common


class RefType(str, enum.Enum):
    Branch = 'branch'
    Tag = 'tag'


@dataclasses.dataclass
class Payload(base.Payload):
    pusher_type: common.PusherType
    ref: str
    ref_type: RefType
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Action = base.Action
Name = base.EventName.Delete
ID = base.ID[Action]
Event = base.Event[ID, Payload]
