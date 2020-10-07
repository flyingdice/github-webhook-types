"""
    ghwht/events/installation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'installation' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#installation
"""
import enum
from datetime import datetime
from typing import Dict, List, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(str, enum.Enum):
    Created = 'created'
    Deleted = 'deleted'
    Suspended = 'suspend'
    Unsuspend = 'unsuspend'


@dataclasses.dataclass
class Installation:
    account: common.Account
    access_tokens_url: HttpUrl
    app_id: int
    app_slug: str
    created_at: datetime
    events: List[str]
    html_url: HttpUrl
    id: int
    permissions: Dict[str, str]
    repository_selection: str
    repositories_url: HttpUrl
    single_file_name: Optional[str]
    suspended_at: Optional[str]
    suspended_by: Optional[str]
    target_id: int
    target_type: common.TargetType
    updated_at: datetime


@dataclasses.dataclass
class Repository:
    full_name: str
    id: int
    node_id: str
    name: str
    private: bool


@dataclasses.dataclass
class Payload(base.Payload):
    installation: Installation
    repositories: List[Repository]
    requester: Optional[str]
    sender: common.Sender


Name = base.EventName.Installation
ID = base.ID[Action]
Event = base.Event[ID, Payload]
