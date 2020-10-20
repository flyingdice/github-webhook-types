"""
    ghwht/hooks/pull_request
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'pull_request' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#pull_request
"""
import enum

from datetime import datetime
from typing import Optional, List

from pydantic import dataclasses, HttpUrl, Field, BaseModel

from . import base, common


class Action(base.Action):
    Assigned = 'assigned'
    Closed = 'closed'
    Edited = 'edited'
    Labeled = 'labeled'
    Locked = 'locked'
    Opened = 'opened'
    ReadyForReview = 'ready_for_review'
    Reopened = 'reopened'
    ReviewRequested = 'review_requested'
    ReviewRequestRemoved = 'review_request_removed'
    Synchronize = 'synchronize'
    Unassigned = 'unassigned'
    Unlabeled = 'unlabeled'
    Unlocked = 'unlocked'


class State(str, enum.Enum):
    All = 'all'
    Closed = 'closed'
    Open = 'open'


class AuthorAssociation(str, enum.Enum):
    Contributor = 'CONTRIBUTOR'
    None_ = 'NONE'
    Owner = 'OWNER'


@dataclasses.dataclass
class Links:
    comments: common.Link
    commits: common.Link
    html: common.Link
    issue: common.Link
    review_comment: common.Link
    review_comments: common.Link
    self: common.Link
    statuses: common.Link


@dataclasses.dataclass
class Changes:
    title: Optional[str]
    body: Optional[str]


class PullRequest(BaseModel):
    active_lock_reason: Optional[str]
    additions: int
    assignee: Optional[common.User]
    assignees: List[common.User]
    author_association: AuthorAssociation
    base: common.Commit
    body: str
    changed_files: int
    closed_at: Optional[datetime]
    comments: int
    comments_url: HttpUrl
    commits: int
    commits_url: HttpUrl
    created_at: datetime
    deletions: int
    diff_url: HttpUrl
    draft: bool
    head: common.Commit
    html_url: HttpUrl
    id: int
    issue_url: HttpUrl
    labels: List[common.Label]
    links: Links = Field(..., alias='_links')
    locked: bool
    maintainer_can_modify: bool
    merge_commit_sha: Optional[str]
    mergeable: Optional[bool]
    mergeable_state: str
    merged: bool
    merged_at: Optional[datetime]
    merged_by: Optional[common.User]
    milestone: Optional[str]
    node_id: str
    number: int
    patch_url: HttpUrl
    rebaseable: Optional[bool]
    requested_reviewers: List[common.Reviewer]
    requested_teams: List[common.Team]
    review_comment_url: HttpUrl
    review_comments: int
    review_comments_url: HttpUrl
    state: State
    statuses_url: HttpUrl
    title: str
    updated_at: datetime
    url: HttpUrl
    user: common.User


@dataclasses.dataclass
class Payload(base.Payload):
    number: int
    pull_request: PullRequest
    repository: common.Repository
    sender: common.Sender

    assignee: Optional[common.Assignee] = None
    installation: Optional[common.Installation] = None
    label: Optional[common.Label] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.PullRequest
ID = base.ID[Action]
Event = base.Event[ID, Payload]
