"""
    ghwht/hooks/check_suite
    ~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'check_suite' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#check_suite
"""
import enum
from datetime import datetime
from typing import List, Optional, Any

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Completed = 'completed'
    Requested = 'requested'
    Rerequested = 'rerequested'


class Status(str, enum.Enum):
    Completed = 'completed'
    InProgress = 'in_progress'
    Queued = 'queued'
    Requested = 'requested'


@dataclasses.dataclass
class Author:
    email: str
    name: str


@dataclasses.dataclass
class Committer:
    email: str
    name: str


@dataclasses.dataclass
class Commit:
    author: Author
    committer: Committer
    id: str
    message: str
    timestamp: str
    tree_id: str


@dataclasses.dataclass
class PullRequestCommit:
    ref: str
    sha: str
    repo: common.Repository


@dataclasses.dataclass
class PullRequest:
    base: PullRequestCommit
    head: PullRequestCommit
    id: int
    number: int
    url: HttpUrl


@dataclasses.dataclass
class Permissions:
    administration: Optional[common.Permission] = None
    checks: Optional[common.Permission] = None
    contents: Optional[common.Permission] = None
    deployments: Optional[common.Permission] = None
    issues: Optional[common.Permission] = None
    members: Optional[common.Permission] = None
    metadata: Optional[common.Permission] = None
    organization_administration: Optional[common.Permission] = None
    organization_hooks: Optional[common.Permission] = None
    organization_plan: Optional[common.Permission] = None
    organization_projects: Optional[common.Permission] = None
    organization_user_blocking: Optional[common.Permission] = None
    pages: Optional[common.Permission] = None
    pull_requests: Optional[common.Permission] = None
    repository_hooks: Optional[common.Permission] = None
    repository_projects: Optional[common.Permission] = None
    statuses: Optional[common.Permission] = None
    team_discussions: Optional[common.Permission] = None
    vulnerability_alerts: Optional[common.Permission] = None


@dataclasses.dataclass
class App:
    created_at: datetime
    description: Optional[str]
    events: List[Any]
    external_url: HttpUrl
    html_url: HttpUrl
    id: int
    name: str
    node_id: str
    owner: common.Owner
    permissions: Permissions
    slug: str
    updated_at: datetime


@dataclasses.dataclass
class CheckSuite:
    app: App
    after: str
    before: str
    check_runs_url: HttpUrl
    conclusion: Optional[common.Conclusion]
    created_at: datetime
    head_commit: Commit
    head_branch: str
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: List[PullRequest]
    status: Status
    updated_at: datetime
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    check_suite: CheckSuite
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.CheckSuite
ID = base.ID[Action]
Event = base.Event[ID, Payload]
