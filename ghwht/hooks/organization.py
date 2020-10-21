"""
    ghwht/hooks/organization
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'organization' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#organization
"""
import enum

from typing import Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Deleted = 'deleted'
    MemberAdded = 'member_added'
    MemberInvited = 'member_invited'
    MemberRemoved = 'member_removed'
    Renamed = 'renamed'


class Role(str, enum.Enum):
    Member = 'member'


class State(str, enum.Enum):
    Pending = 'pending'


@dataclasses.dataclass
class Invitation:
    pass


@dataclasses.dataclass
class Membership:
    organization_url: HttpUrl
    role: Role
    state: State
    url: HttpUrl
    user: common.User


@dataclasses.dataclass
class Payload(base.Payload):
    sender: common.Sender

    installation: Optional[common.Installation] = None
    invitation: Optional[Invitation] = None
    membership: Optional[Membership] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Organization
ID = base.ID[Action]
Event = base.Event[ID, Payload]
