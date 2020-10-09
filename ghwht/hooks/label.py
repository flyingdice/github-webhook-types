"""
    ghwht/hooks/label
    ~~~~~~~~~~~~~~~~~

    Contains types for the 'label' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#label
"""
from typing import Optional

from pydantic import dataclasses, BaseModel, Field

from . import base, common


class Action(base.Action):
    Created = 'created'
    Deleted = 'deleted'
    Edited = 'edited'


class Change(BaseModel):
    from_: str = Field(..., alias='from')


@dataclasses.dataclass
class Changes:
    color: Optional[Change] = None
    description: Optional[Change] = None
    name: Optional[Change] = None


@dataclasses.dataclass
class Payload(base.Payload):
    label: common.Label
    repository: common.Repository
    sender: common.Sender

    changes: Optional[Changes] = None
    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Label
ID = base.ID[Action]
Event = base.Event[ID, Payload]
