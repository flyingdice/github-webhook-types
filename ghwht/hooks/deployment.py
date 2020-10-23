"""
    ghwht/hooks/deployment
    ~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'deployment' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#deployment
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Created = 'created'


@dataclasses.dataclass
class Payload(base.Payload):
    deployment: common.Deployment
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Deployment
ID = base.ID[Action]
Event = base.Event[ID, Payload]
