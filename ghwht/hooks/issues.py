"""
    ghwht/hooks/issues
    ~~~~~~~~~~~~~~~~~~

    Contains types for the 'issues' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#issues
"""
from typing import Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Assigned = 'assigned'
    Closed = 'closed'
    Deleted = 'deleted'
    Demilestoned = 'demilestoned'
    Edited = 'edited'
    Labeled = 'labeled'
    Locked = 'locked'
    Milestoned = 'milestoned'
    Opened = 'opened'
    Pinned = 'pinned'
    Reopened = 'reopened'
    Transferred = 'transferred'
    Unassigned = 'unassigned'
    Unlabled = 'unlabeled'
    Unlocked = 'unlocked'
    Unpinned = 'unpinned'


@dataclasses.dataclass
class Changes:
    body: Optional[common.Change] = None
    title: Optional[common.Change] = None


@dataclasses.dataclass
class Payload(base.Payload):
    issue: common.Issue
    repository: common.Repository
    sender: common.Sender

    assignee: Optional[common.Assignee] = None
    changes: Optional[Changes] = None
    installation: Optional[common.Installation] = None
    label: Optional[common.Label] = None
    milestone: Optional[common.Milestone] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.Issues
ID = base.ID[Action]
Event = base.Event[ID, Payload]
