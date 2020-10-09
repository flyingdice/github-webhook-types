"""
    ghwht/hooks/check_run
    ~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'check_run' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#check_run
"""
import enum
from datetime import datetime
from typing import List, Optional, Any

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Completed = 'completed'
    Created = 'created'
    RequestedAction = 'requested_action'
    Rerequested = 'rerequested'


class Status(str, enum.Enum):
    Completed = 'completed'
    InProgress = 'in_progress'
    Queued = 'queued'


@dataclasses.dataclass
class Output:
    annotations_count: int
    annotations_url: HttpUrl
    summary: Optional[str]
    text: Optional[str]
    title: Optional[str]


@dataclasses.dataclass
class Repository:
    id: int
    name: str
    url: HttpUrl


@dataclasses.dataclass
class Commit:
    ref: str
    repo: Repository
    sha: str


@dataclasses.dataclass
class PullRequest:
    base: Commit
    head: Commit
    id: int
    number: int
    url: HttpUrl


@dataclasses.dataclass
class Permissions:
    administration: str
    checks: str
    contents: str
    deployments: str
    issues: str
    members: str
    metadata: str
    organization_administration: str
    organization_hooks: str
    organization_plan: str
    organization_projects: str
    organization_user_blocking: str
    pages: str
    pull_requests: str
    repository_hooks: str
    repository_projects: str
    statuses: str
    team_discussions: str
    vulnerability_alerts: str


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
    permissions: Optional[Permissions]
    updated_at: datetime


@dataclasses.dataclass
class CheckRun:
    app: App
    completed_at: Optional[datetime]
    conclusion: Optional[common.Conclusion]
    details_url: HttpUrl
    external_id: str
    head_sha: str
    id: int
    name: str
    node_id: str
    output: Output
    started_at: datetime
    status: Status
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    check_run: CheckRun
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.CheckRun
ID = base.ID[Action]
Event = base.Event[ID, Payload]
