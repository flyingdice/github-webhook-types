"""
    ghwht/hooks/member
    ~~~~~~~~~~~~~~~~~~

    Contains types for the 'member' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#member
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Added = 'added'
    Edited = 'edited'
    Removed = 'removed'


@dataclasses.dataclass
class Changes:
    permission: Optional[common.Change] = None


@dataclasses.dataclass
class Payload(base.Payload):
    member: common.Member
    repository: common.Repository
    sender: common.Sender

    changes: Optional[Changes] = None
    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Member
ID = base.ID[Action]
Event = base.Event[ID, Payload]
