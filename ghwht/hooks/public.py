"""
    ghwht/hooks/public
    ~~~~~~~~~~~~~~~~~~

    Contains types for the 'public' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#public
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


@dataclasses.dataclass
class Payload(base.Payload):
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Action = base.Action
Name = base.EventName.Public
ID = base.ID[Action]
Event = base.Event[ID, Payload]
