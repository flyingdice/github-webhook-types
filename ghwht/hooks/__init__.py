"""
    ghwht/hooks
    ~~~~~~~~~~~

    Contains modules for each type of webhook event.
"""
from typing import Dict, Type

from . import (base, check_run, check_suite, create, delete, fork, installation,
               installation_repositories, issue_comment, label, ping, public,
               pull_request, push, release, repository)

__all__ = ['NAME_TO_EVENT', 'Event', 'EventName', 'EventT', 'ID',
           'CheckRunEvent', 'CheckSuiteEvent', 'CreateEvent', 'DeleteEvent',
           'ForkEvent', 'InstallationEvent', 'InstallationRepositoriesEvent',
           'LabelEvent', 'PingEvent', 'PublicEvent', 'PullRequestEvent',
           'PushEvent', 'ReleaseEvent', 'RepositoryEvent']

# Alias base types.
Event = base.Event
EventName = base.EventName
EventT = base.EventT
ID = base.ID
IDT = base.IDT

# Alias concrete event types.
CheckRunEvent = check_run.Event
CheckSuiteEvent = check_suite.Event
CreateEvent = create.Event
DeleteEvent = create.Event
ForkEvent = create.Event
InstallationEvent = installation.Event
InstallationRepositoriesEvent = installation_repositories.Event
IssueCommentEvent = issue_comment.Event
LabelEvent = label.Event
PingEvent = ping.Event
PublicEvent = public.Event
PullRequestEvent = pull_request.Event
PushEvent = push.Event
ReleaseEvent = release.Event
RepositoryEvent = repository.Event


def hooks_modules():
    """
    Generator function that yields all registered webhook event modules.
    """
    yield from (check_run, check_suite, create, delete, fork, installation,
                installation_repositories, issue_comment, label, ping, public,
                pull_request, push, release, repository)


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
