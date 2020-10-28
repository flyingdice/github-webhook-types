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
ActionT = api.ActionT
ID = api.ID

TargetType = api.TargetType

CheckRunEvent = api.CheckRunEvent
CheckSuiteEvent = api.CheckSuiteEvent
CodeScanningAlertEvent = api.CodeScanningAlertEvent
CommitCommentEvent = api.CommitCommentEvent
ContentReferenceEvent = api.ContentReferenceEvent
CreateEvent = api.CreateEvent
DeleteEvent = api.DeleteEvent
DeployKeyEvent = api.DeployKeyEvent
DeploymentEvent = api.DeploymentEvent
DeploymentStatusEvent = api.DeploymentStatusEvent
ForkEvent = api.ForkEvent
GitHubAppAuthorizationEvent = api.GitHubAppAuthorizationEvent
InstallationEvent = api.InstallationEvent
InstallationRepositoriesEvent = api.InstallationRepositoriesEvent
IssueCommentEvent = api.IssueCommentEvent
IssuesEvent = api.IssuesEvent
LabelEvent = api.LabelEvent
MarketplacePurchaseEvent = api.MarketplacePurchaseEvent
MemberEvent = api.MemberEvent
MembershipEvent = api.MembershipEvent
MetaEvent = api.MetaEvent
MilestoneEvent = api.MilestoneEvent
OrganizationEvent = api.OrganizationEvent
PingEvent = api.PingEvent
PublicEvent = api.PublicEvent
PullRequestEvent = api.PullRequestEvent
PushEvent = api.PushEvent
ReleaseEvent = api.ReleaseEvent
RepositoryEvent = api.RepositoryEvent
SecurityAdvisoryEvent = api.SecurityAdvisoryEvent


__all__ = api.ALL
__author__ = meta.AUTHOR
__version__ = meta.VERSION
