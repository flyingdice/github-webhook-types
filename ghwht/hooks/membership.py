"""
    ghwht/hooks/membership
    ~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'membership' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#membership
"""
import enum

from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Added = 'added'
    Removed = 'removed'


class Scope(str, enum.Enum):
    Team = 'team'


@dataclasses.dataclass
class Payload(base.Payload):
    member: common.Member
    repository: common.Repository
    scope: Scope
    sender: common.Sender
    team: common.Team

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Membership
ID = base.ID[Action]
Event = base.Event[ID, Payload]
