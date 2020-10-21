"""
    ghwht/events/meta
    ~~~~~~~~~~~~~~~~~

    Contains types for the 'meta' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#meta
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Deleted = 'deleted'


@dataclasses.dataclass
class Payload(base.Payload):
    hook: common.Hook
    hook_id: int
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Meta
ID = base.ID[Action]
Event = base.Event[ID, Payload]
