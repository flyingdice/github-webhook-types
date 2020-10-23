"""
    ghwht/hooks/deployment
    ~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'deployment' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#deployment
"""
from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'


@dataclasses.dataclass
class Payload:
    pass


@dataclasses.dataclass
class Deployment:
    created_at: datetime
    creator: common.Creator
    description: Optional[str]
    environment: str
    id: int
    node_id: str
    original_environment: str
    payload: Dict[str, Any]
    ref: str
    repository_url: HttpUrl
    sha: str
    statuses_url: HttpUrl
    task: str
    updated_at: datetime
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    deployment: Deployment
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Deployment
ID = base.ID[Action]
Event = base.Event[ID, Payload]
