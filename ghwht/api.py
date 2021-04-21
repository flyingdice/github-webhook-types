"""
    ghwht/api
    ~~~~~~~~~

    Defines the public API for the `ghwht` package.
"""
import uuid

from typing import Optional

from . import hooks

# Defines public package interface __all__.
ALL = [
    'new_event',
    'new_id',
    'is_access_revoked',
    'Event',
    'EventName',
    'EventT',
    'ActionT',
    'ID',
    'EventRemovesIntegrationAccess',
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
    'OrganizationEvent',
    'PingEvent',
    'PublicEvent',
    'PullRequestEvent',
    'PushEvent',
    'ReleaseEvent',
    'RepositoryEvent',
    'SecurityAdvisoryEvent'
]

# Export common base types.
Event = hooks.Event
EventName = hooks.EventName
EventT = hooks.EventT
ActionT = hooks.ActionT
ID = hooks.ID

# Export enum types.
TargetType = hooks.TargetType

# Export concrete event types.
CheckRunEvent = hooks.CheckRunEvent
CheckSuiteEvent = hooks.CheckSuiteEvent
CodeScanningAlertEvent = hooks.CodeScanningAlertEvent
CommitCommentEvent = hooks.CommitCommentEvent
ContentReferenceEvent = hooks.ContentReferenceEvent
CreateEvent = hooks.CreateEvent
DeleteEvent = hooks.DeleteEvent
DeployKeyEvent = hooks.DeployKeyEvent
DeploymentEvent = hooks.DeploymentEvent
DeploymentStatusEvent = hooks.DeploymentStatusEvent
ForkEvent = hooks.ForkEvent
GitHubAppAuthorizationEvent = hooks.GitHubAppAuthorizationEvent
InstallationEvent = hooks.InstallationEvent
InstallationRepositoriesEvent = hooks.InstallationRepositoriesEvent
IssueCommentEvent = hooks.IssueCommentEvent
IssuesEvent = hooks.IssuesEvent
LabelEvent = hooks.LabelEvent
MarketplacePurchaseEvent = hooks.MarketplacePurchaseEvent
MemberEvent = hooks.MemberEvent
MembershipEvent = hooks.MembershipEvent
MetaEvent = hooks.MetaEvent
MilestoneEvent = hooks.MilestoneEvent
OrganizationEvent = hooks.OrganizationEvent
PingEvent = hooks.PingEvent
PublicEvent = hooks.PublicEvent
PullRequestEvent = hooks.PullRequestEvent
PushEvent = hooks.PushEvent
ReleaseEvent = hooks.ReleaseEvent
RepositoryEvent = hooks.RepositoryEvent
SecurityAdvisoryEvent = hooks.SecurityAdvisoryEvent


def new_event(delivery_id: uuid.UUID,
              event_name: str,
              hook_id: int,
              action: Optional[str],
              payload: dict) -> hooks.EventT:
    """
    Create an event instance for the given data.

    The type of Event returned is determined by the event name/action of the request.

    :param delivery_id: UUID of the delivery
    :param event_name: Name of the event
    :param hook_id: ID of the webhook
    :param action: Action of the event
    :param payload: Event data payload
    :return: Event
    """
    name = hooks.EventName(event_name)

    id_cls = hooks.NAME_TO_ID[name]
    event_cls = hooks.NAME_TO_EVENT[name]

    return event_cls(
        id=id_cls(
            name=name,
            action=action
        ),
        delivery_id=delivery_id,
        hook_id=hook_id,
        payload=payload
    )


def new_id(value: str) -> ID:
    """
    Create an ID instance for the given string.

    The string will be in the format '{event_name}.{action}'
    where 'action' is optional.

    Ex: 'issues.created' or 'ping'

    :param value: Value to convert to ID
    :return: ID
    """
    event_name, *extras = value.split('.')

    name = hooks.EventName(event_name)
    return hooks.NAME_TO_ID[name](
        name=name,
        action=extras[0] if len(extras) else None
    )


# List of event ID's that indicate we no longer have integration API access when received.
INTEGRATION_ACCESS_REMOVED_EVENTS = frozenset((
    new_id('installation.suspend'),
    new_id('installation.deleted')
))


def is_access_revoked(event: EventT) -> bool:
    """
    Return True if the given event indicates that access has been revoked.

    This happens for the following GitHub events:
    * installation.suspend
    * installation.deleted

    :param event: Event to check
    :return: True if access has been revoked, False otherwise
    """
    return event.id in INTEGRATION_ACCESS_REMOVED_EVENTS
