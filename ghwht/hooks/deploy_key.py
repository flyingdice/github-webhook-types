"""
    ghwht/hooks/deploy_key
    ~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'deploy_key' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#deploy_key
"""
from datetime import datetime
from typing import Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'
    Deleted = 'deleted'


@dataclasses.dataclass
class Key:
    created_at: datetime
    id: int
    key: str
    read_only: bool
    title: str
    url: HttpUrl
    verified: bool


@dataclasses.dataclass
class Payload(base.Payload):
    key: Key
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.DeployKey
ID = base.ID[Action]
Event = base.Event[ID, Payload]
