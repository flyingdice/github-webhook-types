"""
    ghwht/hooks/deployment_status
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'deployment_status' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#deployment_status
"""
import enum

from datetime import datetime
from typing import Optional, Union

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'


class State(str, enum.Enum):
    Error = 'error'
    Failure = 'failure'
    Inactive = 'inactgive'
    InProgress = 'in_progress'
    Queued = 'queued'
    Pending = 'pending'
    Success = 'success'


@dataclasses.dataclass
class DeploymentStatus:
    created_at: datetime
    creator: common.Creator
    description: Optional[str]
    deployment_url: HttpUrl
    environment: str
    id: int
    node_id: str
    repository_url: HttpUrl
    state: State
    target_url: Union[str, HttpUrl]
    updated_at: datetime
    url: HttpUrl


@dataclasses.dataclass
class Payload(base.Payload):
    deployment: common.Deployment
    deployment_status: DeploymentStatus
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.DeploymentStatus
ID = base.ID[Action]
Event = base.Event[ID, Payload]
