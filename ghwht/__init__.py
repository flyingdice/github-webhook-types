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
ContentReferenceEvent = api.ContentReferenceEvent
CreateEvent = api.CreateEvent
DeleteEvent = api.DeleteEvent
DeployKeyEvent = api.DeployKeyEvent
ForkEvent = api.ForkEvent
InstallationEvent = api.InstallationEvent
InstallationRepositoriesEvent = api.InstallationRepositoriesEvent
IssueCommentEvent = api.IssueCommentEvent
IssuesEvent = api.IssuesEvent
LabelEvent = api.LabelEvent
MarketplacePurchaseEvent = api.MarketplacePurchaseEvent
MemberEvent = api.MemberEvent
MembershipEvent = api.MembershipEvent
PingEvent = api.PingEvent
PublicEvent = api.PublicEvent
PullRequestEvent = api.PullRequestEvent
PushEvent = api.PushEvent
ReleaseEvent = api.ReleaseEvent
RepositoryEvent = api.RepositoryEvent


__all__ = api.ALL
__author__ = meta.AUTHOR
__version__ = meta.VERSION
