"""
    ghwht/hooks/installation_repositories
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'installation_repositories' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#installation_repositories
"""
import enum
from datetime import datetime
from typing import List, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Added = 'added'
    Removed = 'removed'


class RepositorySelection(str, enum.Enum):
    All = 'all'
    Selected = 'selected'


@dataclasses.dataclass
class RepositoryAdded:
    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


@dataclasses.dataclass
class RepositoryRemoved:
    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


@dataclasses.dataclass
class Installation:
    account: common.Account
    access_tokens_url: HttpUrl
    app_id: int
    app_slug: str
    created_at: datetime
    events: List[base.EventName]
    html_url: HttpUrl
    id: int
    permissions: common.InstallationPermissions
    repository_selection: common.RepositorySelection
    repositories_url: HttpUrl
    single_file_name: Optional[str]
    suspended_at: Optional[str]
    suspended_by: Optional[str]
    target_id: int
    target_type: common.TargetType
    updated_at: datetime


@dataclasses.dataclass
class Payload(base.Payload):
    installation: Installation
    repository_selection: common.RepositorySelection
    repositories_added: List[RepositoryAdded]
    repositories_removed: List[RepositoryRemoved]
    sender: common.Sender

    organization: Optional[common.Organization] = None
    requester: Optional[str] = None


Name = base.EventName.InstallationRepositories
ID = base.ID[Action]
Event = base.Event[ID, Payload]
