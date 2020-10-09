"""
    ghwht/hooks/repository
    ~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'repository' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#repository
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Archived = 'archived'
    Created = 'created'
    Deleted = 'deleted'
    Edited = 'edited'
    Privatized = 'privatized'
    Publicized = 'publicized'
    Renamed = 'renamed'
    Transferred = 'transferred'
    Unarchived = 'unarchived'


@dataclasses.dataclass
class Payload(base.Payload):
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Repository
ID = base.ID[Action]
Event = base.Event[ID, Payload]
