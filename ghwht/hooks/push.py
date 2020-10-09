"""
    ghwht/hooks/push
    ~~~~~~~~~~~~~~~~

    Contains types for the 'push' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#push
"""
from datetime import datetime
from typing import Optional, List

from pydantic import dataclasses, HttpUrl

from . import base, common


@dataclasses.dataclass
class Organization:
    avatar_url: HttpUrl
    created_at: datetime
    description: Optional[str]
    events_url: HttpUrl
    followers: int
    following: int
    has_organization_projects: bool
    has_repository_projects: bool
    hooks_url: HttpUrl
    html_url: HttpUrl
    id: int
    issues_url: HttpUrl
    is_verified: bool
    login: str
    members_url: HttpUrl
    name: str
    node_id: str
    public_gists: int
    public_members_url: HttpUrl
    public_repos: int
    repos_url: HttpUrl
    type: common.TargetType
    updated_at: datetime
    url: HttpUrl

    blog: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None
    twitter_username: Optional[str] = None


@dataclasses.dataclass
class Author:
    email: str
    name: str
    username: str


@dataclasses.dataclass
class Committer:
    email: str
    name: str
    username: str


@dataclasses.dataclass
class Commit:
    added: List[str]
    author: Author
    committer: Committer
    distinct: bool
    id: str
    message: str
    modified: List[str]
    removed: List[str]
    tree_id: str
    timestamp: datetime
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    after: str
    base_ref: Optional[str]
    before: str
    commits: List[Commit]
    compare: str
    created: bool
    deleted: bool
    forced: bool
    head_commit: Optional[Commit]
    pusher: common.Pusher
    ref: str
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Action = base.Action
Name = base.EventName.Push
ID = base.ID[Action]
Event = base.Event[ID, Payload]
