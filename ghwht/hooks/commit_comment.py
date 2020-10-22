"""
    ghwht/events/commit_comment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'commit_comment' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#commit_comment
"""
from datetime import datetime
from typing import Optional

from pydantic import dataclasses, HttpUrl

from . import base, common


class Action(base.Action):
    Created = 'created'


@dataclasses.dataclass
class Comment:
    author_association: common.AuthorAssociation
    body: str
    commit_id: str
    created_at: datetime
    html_url: HttpUrl
    id: int
    issue_url: HttpUrl
    line: Optional[int]
    node_id: str
    path: Optional[str]
    position: Optional[int]
    updated_at: datetime
    url: HttpUrl
    user: common.User


@dataclasses.dataclass
class Payload(base.Payload):
    comment: Comment
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None


Name = base.EventName.CommitComment
ID = base.ID[Action]
Event = base.Event[ID, Payload]


