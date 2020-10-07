"""
    ghwht/events/ping
    ~~~~~~~~~~~~~~~~~

    Contains types for the 'ping' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#ping
"""
from datetime import datetime
from typing import List

from pydantic import dataclasses, HttpUrl

from . import base


@dataclasses.dataclass
class HookConfig:
    content_type: str
    insecure_ssl: str
    url: HttpUrl


@dataclasses.dataclass
class Hook:
    active: bool
    app_id: str
    config: HookConfig
    created_at: datetime
    events: List[str]
    id: int
    name: str
    type: str
    updated_at: datetime


@dataclasses.dataclass
class Payload(base.EmptyPayload):
    hook: Hook
    hook_id: int
    zen: str


Name = base.EventName.Ping
ID = base.ID[base.Action]
Event = base.Event[ID, Payload]
