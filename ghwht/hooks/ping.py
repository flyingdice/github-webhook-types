"""
    ghwht/events/ping
    ~~~~~~~~~~~~~~~~~

    Contains types for the 'ping' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#ping
"""
from pydantic import dataclasses

from . import base, common


@dataclasses.dataclass
class Payload(base.Payload):
    hook: common.Hook
    hook_id: int
    zen: str


Action = base.Action
Name = base.EventName.Ping
ID = base.ID[Action]
Event = base.Event[ID, Payload]
