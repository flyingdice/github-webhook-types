"""
    ghwht/events/code_scanning_alert
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'code_scanning_alert' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#code_scanning_alert
"""
import enum
from datetime import datetime
from typing import List, Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    AppearedInBranch = 'appeared_in_branch'
    Created = 'created'
    ClosedByUser = 'closed_by_user'
    Fixed = 'fixed'
    ReopenedByUser = 'reopened_by_user'
    Reopened = 'reopened'


class State(str, enum.Enum):
    Open = 'open'


class Severity(str, enum.Enum):
    Note = 'note'


@dataclasses.dataclass
class Rule:
    description: Optional[str]
    id: str
    severity: Severity


@dataclasses.dataclass
class Tool:
    name: str
    version: Optional[str]


@dataclasses.dataclass
class Instance:
    analysis_key: str
    environment: str
    ref: str
    state: State


@dataclasses.dataclass
class Alert:
    created_at: datetime
    dismissed_by: Optional[common.Account]
    dismissed_at: Optional[datetime]
    dismissed_reason: Optional[str]
    number: int
    instances: List[int]
    rule: Rule
    tool: Tool
    state: State
    html_url: HttpUrl
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    alert: Alert
    ref: str
    repository: common.Repository
    sender: common.Sender

    commit_oid: Optional[str] = None
    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.CodeScanningAlert
ID = base.ID[Action]
Event = base.Event[ID, Payload]


