"""
    ghwht
    ~~~~~

    Type definitons for GitHub webhooks.
"""
from . import api, meta

new_event = api.new_event
new_id = api.new_id
Event = api.Event
EventName = api.EventName
EventT = api.EventT
ID = api.ID

CheckRunEvent = api.CheckRunEvent
CheckSuiteEvent = api.CheckSuiteEvent
CreateEvent = api.CreateEvent
DeleteEvent = api.DeleteEvent
ForkEvent = api.ForkEvent
InstallationEvent = api.InstallationEvent
InstallationRepositoriesEvent = api.InstallationRepositoriesEvent
LabelEvent = api.LabelEvent
PingEvent = api.PingEvent
PublicEvent = api.PublicEvent
PullRequestEvent = api.PullRequestEvent
PushEvent = api.PushEvent
ReleaseEvent = api.ReleaseEvent
RepositoryEvent = api.RepositoryEvent


__all__ = api.__all__
__author__ = meta.AUTHOR
__version__ = meta.VERSION
