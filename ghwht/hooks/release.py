"""
    ghwht/hooks/release
    ~~~~~~~~~~~~~~~~~~~

    Contains types for the 'release' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#release
"""
import enum
from datetime import datetime
from typing import Any, Optional, List

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(str, enum.Enum):
    Created = 'created'
    Deleted = 'deleted'
    Edited = 'edited'
    PreReleased = 'prereleased'
    Published = 'published'
    Released = 'released'
    Unpublished = 'unpublished'


@dataclasses.dataclass
class Asset:
    pass


@dataclasses.dataclass
class Release:
    assets_url: HttpUrl
    assets: List[Any]
    author: common.Author
    body: str
    created_at: datetime
    draft: bool
    html_url: HttpUrl
    id: int
    name: str
    node_id: str
    prerelease: bool
    published_at: datetime
    tag_name: str
    tarball_url: HttpUrl
    target_commitish: str
    upload_url: HttpUrl
    url: HttpUrl
    zipball_url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    release: Release
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Release
ID = base.ID[Action]
Event = base.Event[ID, Payload]
