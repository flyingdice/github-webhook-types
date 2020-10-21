"""
    ghwht/hooks/issue_comment
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'issue_comment' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#issue_comment
"""
from datetime import datetime
from typing import List, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'
    Deleted = 'deleted'
    Edited = 'edited'


@dataclasses.dataclass
class Changes:
    body: Optional[common.Change] = None


@dataclasses.dataclass
class Issue:
    assignee: Optional[common.Assignee]
    assignees: List[common.Assignee]
    author_association: common.AuthorAssociation
    body: str
    closed_at: Optional[datetime]
    comments: int
    comments_url: HttpUrl
    created_at: datetime
    events_url: HttpUrl
    html_url: HttpUrl
    id: int
    labels: List[common.Label]
    labels_url: HttpUrl
    locked: bool
    milestone: Optional[common.Milestone]
    node_id: str
    number: int
    repository_url: HttpUrl
    state: common.State
    title: str
    updated_at: datetime
    url: HttpUrl
    user: common.User

    active_lock_reason: Optional[str] = None
    performed_via_github_app: Optional[bool] = None


@dataclasses.dataclass
class Comment:
    author_association: common.AuthorAssociation
    body: str
    created_at: datetime
    html_url: HttpUrl
    id: int
    issue_url: HttpUrl
    node_id: str
    updated_at: datetime
    url: HttpUrl
    user: common.User

    performed_via_github_app: Optional[bool] = None


@dataclasses.dataclass
class Payload(base.Payload):
    comment: Comment
    issue: Issue
    repository: common.Repository
    sender: common.Sender

    changes: Optional[Changes] = None
    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.IssueComment
ID = base.ID[Action]
Event = base.Event[ID, Payload]
