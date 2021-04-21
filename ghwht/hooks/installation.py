"""
    ghwht/events/installation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'installation' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#installation
"""
from datetime import datetime
from typing import List, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'
    Deleted = 'deleted'
    NewPermissionsAccepted = 'new_permissions_accepted'
    Suspended = 'suspend'
    Unsuspend = 'unsuspend'


@dataclasses.dataclass
class Installation:
    account: common.Account
    access_tokens_url: HttpUrl
    app_id: int
    app_slug: str
    created_at: datetime
    events: List[base.EventName]
    has_multiple_single_files: Optional[bool]
    html_url: HttpUrl
    id: int
    permissions: common.InstallationPermissions
    repository_selection: common.RepositorySelection
    repositories_url: HttpUrl
    single_file_name: Optional[str]
    single_file_paths: List[str]
    suspended_at: Optional[datetime]
    suspended_by: Optional[common.User]
    target_id: int
    target_type: common.TargetType
    updated_at: datetime


@dataclasses.dataclass
class Repository:
    full_name: str
    id: int
    node_id: str
    name: str
    private: bool


@dataclasses.dataclass
class Payload(base.Payload):
    installation: Installation
    sender: common.Sender

    repositories: List[Repository] = None
    requester: Optional[str] = None


Name = base.EventName.Installation
ID = base.ID[Action]
Event = base.Event[ID, Payload]
