"""
    ghwht/hooks/common
    ~~~~~~~~~~~~~~~~~~

    Contains common types used in many webhook events.
"""
from datetime import datetime
import enum
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, dataclasses


class Conclusion(str, enum.Enum):
    ActionRequired = 'action_required'
    Cancelled = 'cancelled'
    Failure = 'failure'
    Neutral = 'neutral'
    State = 'stale'
    Success = 'success'
    TimedOut = 'timed_out'


class Event(str, enum.Enum):
    CheckRun = 'check_run'
    CheckSuite = 'check_suite'
    CommitComment = 'commit_comment'
    Create = 'create'
    Delete = 'delete'
    Fork = 'fork'
    Gollum = 'gollum'
    Label = 'label'
    Milestone = 'milestone'
    Public = 'public'
    PullRequest = 'pull_request'
    PullRequestReview = 'pull_request_review'
    PullRequestReviewComment = 'pull_request_review_comment'
    Push = 'push'
    Release = 'release'
    Repository = 'repository'
    RepositoryDispatch = 'repository_dispatch'
    Star = 'star'
    Status = 'status'
    Watch = 'watch'
    WorkflowDispatch = 'workflow_dispatch'
    WorkflowRun = 'workflow_run'


class Permission(str, enum.Enum):
    Read = 'read'
    Write = 'write'


class PusherType(str, enum.Enum):
    Bot = 'bot'
    User = 'user'


class TargetType(str, enum.Enum):
    User = 'User'
    Repository = 'Repository'
    Organization = 'Organization'


@dataclasses.dataclass
class Account:
    avatar_url: HttpUrl
    events_url: HttpUrl
    followers_url: HttpUrl
    following_url: HttpUrl
    gists_url: HttpUrl
    gravatar_id: str
    html_url: HttpUrl
    id: int
    login: str
    node_id: str
    organizations_url: HttpUrl
    received_events_url: HttpUrl
    repos_url: HttpUrl
    site_admin: bool
    starred_url: HttpUrl
    subscriptions_url: HttpUrl
    type: TargetType
    url: HttpUrl

    email: Optional[str] = None
    name: Optional[str] = None


Assignee = Account
Author = Account
Owner = Account
Pusher = Account
Reviewer = Account
Sender = Account
User = Account


class Change(BaseModel):
    from_: str = Field(..., alias='from')


@dataclasses.dataclass
class Installation:
    id: int
    node_id: str


@dataclasses.dataclass
class InstallationPermissions:
    administration: Optional[Permission] = None
    checks: Optional[Permission] = None
    contents: Optional[Permission] = None
    deployments: Optional[Permission] = None
    issues: Optional[Permission] = None
    metadata: Optional[Permission] = None
    pages: Optional[Permission] = None
    pull_requests: Optional[Permission] = None
    repository_hooks: Optional[Permission] = None
    repository_projects: Optional[Permission] = None
    statuses: Optional[Permission] = None
    vulnerability_alerts: Optional[Permission] = None


@dataclasses.dataclass
class License:
    key: str
    name: str
    node_id: str
    spdx_id: str
    url: HttpUrl


@dataclasses.dataclass
class Organization:
    avatar_url: HttpUrl
    description: Optional[str]
    events_url: HttpUrl
    hooks_url: HttpUrl
    id: int
    issues_url: HttpUrl
    login: str
    members_url: HttpUrl
    node_id: str
    public_members_url: HttpUrl
    repos_url: HttpUrl
    url: HttpUrl


@dataclasses.dataclass
class Permissions:
    admin: bool
    pull: bool
    push: bool


@dataclasses.dataclass
class Pusher:
    email: str
    name: str


@dataclasses.dataclass
class Repository:
    archived: bool
    archive_url: HttpUrl
    assignees_url: HttpUrl
    blobs_url: HttpUrl
    branches_url: HttpUrl
    clone_url: HttpUrl
    collaborators_url: HttpUrl
    commits_url: HttpUrl
    comments_url: HttpUrl
    compare_url: HttpUrl
    contents_url: HttpUrl
    contributors_url: HttpUrl
    created_at: datetime
    default_branch: str
    deployments_url: HttpUrl
    description: Optional[str]
    disabled: bool
    downloads_url: HttpUrl
    events_url: HttpUrl
    fork: bool
    forks: int
    forks_count: int
    forks_url: HttpUrl
    full_name: str
    git_commits_url: HttpUrl
    git_refs_url: HttpUrl
    git_tags_url: HttpUrl
    git_url: str  # TODO
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    homepage: Optional[str]
    hooks_url: HttpUrl
    html_url: HttpUrl
    owner: Owner
    language: Optional[str]
    languages_url: HttpUrl
    labels_url: HttpUrl
    license: Optional[License]
    id: int
    issue_comment_url: HttpUrl
    issue_events_url: HttpUrl
    issues_url: HttpUrl
    keys_url: HttpUrl
    merges_url: HttpUrl
    milestones_url: HttpUrl
    mirror_url: Optional[HttpUrl]
    name: str
    node_id: str
    notifications_url: HttpUrl
    open_issues: int
    open_issues_count: int
    private: bool
    pulls_url: HttpUrl
    pushed_at: Optional[datetime]
    releases_url: HttpUrl
    size: int
    ssh_url: str  # TODO
    stargazers_count: int
    stargazers_url: HttpUrl
    statuses_url: HttpUrl
    subscribers_url: HttpUrl
    subscription_url: HttpUrl
    svn_url: HttpUrl
    tags_url: HttpUrl
    teams_url: HttpUrl
    trees_url: HttpUrl
    updated_at: datetime
    url: HttpUrl
    watchers: int
    watchers_count: int

    allow_squash_merge: Optional[bool] = None
    allow_merge_commit: Optional[bool] = None
    allow_rebase_merge: Optional[bool] = None
    delete_branch_on_merge: Optional[bool] = None
    master_branch: Optional[str] = None
    organization: Optional[str] = None
    public: Optional[bool] = None
    permissions: Optional[Permissions] = None
    stargazers: Optional[int] = None


class RepositorySelection(str, enum.Enum):
    All = 'all'
    Selected = 'selected'


@dataclasses.dataclass
class Commit:
    label: str
    ref: str
    repo: Repository
    sha: str
    user: User


@dataclasses.dataclass
class Link:
    href: HttpUrl


@dataclasses.dataclass
class Team:
    pass


@dataclasses.dataclass
class Label:
    color: str
    default: bool
    description: str
    id: int
    name: str
    node_id: str
    url: HttpUrl
