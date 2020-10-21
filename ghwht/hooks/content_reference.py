"""
    ghwht/hooks/content_reference
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'content_reference' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#content_reference
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Created = 'created'


@dataclasses.dataclass
class ContentReference:
    id: int
    node_id: str
    reference: str


@dataclasses.dataclass
class Payload(base.Payload):
    content_reference: ContentReference
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.ContentReference
ID = base.ID[Action]
Event = base.Event[ID, Payload]
