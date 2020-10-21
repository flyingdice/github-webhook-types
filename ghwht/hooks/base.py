"""
    ghwht/hooks/base
    ~~~~~~~~~~~~~~~~

    Contains types generic to all GitHub webhooks.
"""
import enum

from typing import Generic, Optional, TypeVar
from uuid import UUID

from pydantic import dataclasses, generics


class EventName(str, enum.Enum):
    """
    Enumeration for all known GitHub webhook events.
    """
    CheckRun = 'check_run'
    CheckSuite = 'check_suite'
    CodeScanningAlert = 'code_scanning_alert'
    CommitComment = 'commit_comment'
    ContentReference = 'content_reference'
    Create = 'create'
    Delete = 'delete'
    DeployKey = 'deploy_key'
    Deployment = 'deployment'
    DeploymentStatus = 'deployment_status'
    Fork = 'fork'
    GithubAppAuthorization = 'github_app_authorization'
    Gollum = 'gollum'
    Installation = 'installation'
    InstallationRepositories = 'installation_repositories'
    IssueComment = 'issue_comment'
    Issues = 'issues'
    Label = 'label'
    MarketplacePurchase = 'marketplace_purchase'
    Member = 'member'
    Membership = 'membership'
    Meta = 'meta'
    Milestone = 'milestone'
    Organization = 'organization'
    OrganizationBlock = 'org_block'
    Package = 'package'
    PageBuild = 'page_build'
    Ping = 'ping'
    ProjectCard = 'project_card'
    ProjectColumn = 'project_column'
    Project = 'project'
    Public = 'public'
    PullRequest = 'pull_request'
    PullRequestReview = 'pull_request_review'
    PullRequestReviewComment = 'pull_request_review_comment'
    Push = 'push'
    Release = 'release'
    RepositoryDispatch = 'repository_dispatch'
    Repository = 'repository'
    RepositoryImport = 'repository_import'
    RepositoryVulnerabilityAlert = 'repository_vulnerability_alert'
    SecurityAdvisory = 'security_advisory'
    Sponsorship = 'sponsorship'
    Star = 'star'
    Status = 'status'
    Team = 'team'
    TeamAdd = 'team_add'
    Watch = 'watch'
    WorkflowDispatch = 'workflow_dispatch'
    WorkflowRun = 'workflow_run'


class Action(enum.Enum):
    """
    Represents a Github event action.

    This is a marker class so we can apply inheritance constraints on generic
    types and can never implement actual enumeration values. Abstract in the strictest sense.
    """


# Generic type var for types derived from :class:`~ghwht.hooks.base.Action`.
ActionT = TypeVar('ActionT', bound=Action)


@dataclasses.dataclass
class Payload:
    """
    Represents a Github event payload.

    This is a marker class so we can apply inheritance constraints on generic
    types and shouldn't implement any fields.
    """


# Generic type var for types derived from :class:`~ghwht.hooks.base.Payload`.
PayloadT = TypeVar('PayloadT', bound=Payload)


class ID(generics.GenericModel, Generic[ActionT]):
    """
    Represents an identifier for a specific event/action combination.

    Actions are optional for certain events, e.g. 'ping' while required for others
    e.g. 'issues.created'.
    """
    event_name: EventName
    action: Optional[ActionT]

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return '.'.join((p.value for p in (self.event_name, self.action) if p))


# Generic type var for types derived from :class:`~ghwht.hooks.base.ID`.
IDT = TypeVar('IDT', bound=ID)


class Event(generics.GenericModel, Generic[IDT, PayloadT]):
    """
    Represents an abstract Github webhook event.

    All known GitHub webhook events should derive from this class and specify the
    event 'name' that they should be parsed from.

    Event models encapsulate information that comes in both the webhook request payload
    and HTTP headers.
    """
    id: IDT
    delivery_id: UUID
    hook_id: int
    payload: PayloadT


# Generic type var for types derived from :class:`~ghwht.hooks.base.Event`.
EventT = TypeVar('EventT', bound=Event)
