"""
    ghwht/hooks/milestone
    ~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'milestone' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#milestone
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Created = 'created'
    Closed = 'closed'
    Deleted = 'deleted'
    Edited = 'edited'
    Opened = 'opened'


@dataclasses.dataclass
class Changes:
    description: Optional[common.Change] = None
    due_on: Optional[common.Change] = None
    title: Optional[common.Change] = None


@dataclasses.dataclass
class Payload(base.Payload):
    milestone: common.Milestone
    repository: common.Repository
    sender: common.Sender

    changes: Optional[Changes] = None
    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Milestone
ID = base.ID[Action]
Event = base.Event[ID, Payload]
