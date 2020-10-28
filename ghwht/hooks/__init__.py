"""
    ghwht/hooks
    ~~~~~~~~~~~

    Contains modules for each type of webhook event.
"""
from typing import Dict, Type

from . import (base, check_run, check_suite, code_scanning_alert, commit_comment, common,
               content_reference, create, delete, deploy_key, deployment, deployment_status,
               fork, github_app_authorization, installation, installation_repositories,
               issue_comment, issues, label, marketplace_purchase, member, membership, meta,
               milestone, organization, ping, public, pull_request, push, release, repository,
               security_advisory)

__all__ = [
    'NAME_TO_EVENT',
    'Event',
    'EventName',
    'EventT',
    'ActionT',
    'ID',
    'CheckRunEvent',
    'CheckSuiteEvent',
    'CodeScanningAlertEvent',
    'CommitCommentEvent',
    'ContentReferenceEvent',
    'CreateEvent',
    'DeleteEvent',
    'DeployKeyEvent',
    'DeploymentEvent',
    'DeploymentStatusEvent',
    'ForkEvent',
    'GitHubAppAuthorizationEvent',
    'InstallationEvent',
    'InstallationRepositoriesEvent',
    'LabelEvent',
    'MarketplacePurchaseEvent',
    'MemberEvent',
    'MembershipEvent',
    'MetaEvent',
    'MilestoneEvent',
    'PingEvent',
    'PublicEvent',
    'PullRequestEvent',
    'PushEvent',
    'OrganizationEvent',
    'ReleaseEvent',
    'RepositoryEvent',
    'SecurityAdvisoryEvent'
]

# Alias base types.
Event = base.Event
EventName = base.EventName
EventT = base.EventT
ActionT = base.ActionT
ID = base.ID
IDT = base.IDT

# Export enum types.
TargetType = common.TargetType

# Alias concrete event types.
CheckRunEvent = check_run.Event
CheckSuiteEvent = check_suite.Event
CodeScanningAlertEvent = code_scanning_alert.Event
CommitCommentEvent = commit_comment.Event
ContentReferenceEvent = content_reference.Event
CreateEvent = create.Event
DeleteEvent = delete.Event
DeployKeyEvent = deploy_key.Event
DeploymentEvent = deployment.Event
DeploymentStatusEvent = deployment_status.Event
ForkEvent = create.Event
GitHubAppAuthorizationEvent = github_app_authorization.Event
InstallationEvent = installation.Event
InstallationRepositoriesEvent = installation_repositories.Event
IssueCommentEvent = issue_comment.Event
IssuesEvent = issues.Event
LabelEvent = label.Event
MarketplacePurchaseEvent = marketplace_purchase.Event
MemberEvent = member.Event
MembershipEvent = membership.Event
MetaEvent = meta.Event
MilestoneEvent = milestone.Event
PingEvent = ping.Event
PublicEvent = public.Event
PullRequestEvent = pull_request.Event
PushEvent = push.Event
OrganizationEvent = organization.Event
ReleaseEvent = release.Event
RepositoryEvent = repository.Event


def hooks_modules():
    """
    Generator function that yields all registered webhook event modules.
    """
    yield from (check_run, check_suite, code_scanning_alert, content_reference,
                create, delete, deploy_key, deployment, deployment_status, fork,
                github_app_authorization, installation, installation_repositories,
                issue_comment, issues, label, marketplace_purchase, member, membership,
                milestone, organization, ping, public, pull_request, push, release, repository)


# Lookup table that maps event names to their appropriate identifier type.
# Ex: 'issues' -> ghwht.hooks.issues.Identifier.
NAME_TO_ID: Dict[EventName, Type[IDT]] = dict(
    (module.Name, module.ID)
    for module in hooks_modules()
)


# Lookup table that maps event names to their appropriate type.
# Ex: 'issues' -> ghwht.hooks.issues.Event.
NAME_TO_EVENT: Dict[EventName, Type[EventT]] = dict(
    (module.Name, module.Event)
    for module in hooks_modules()
)
