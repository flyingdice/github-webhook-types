"""
    ghwht/hooks/github_app_authorization
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'github_app_authorization' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#github_app_authorization
"""
from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Revoked = 'revoked'


@dataclasses.dataclass
class Payload(base.Payload):
    sender: common.Sender


Name = base.EventName.GithubAppAuthorization
ID = base.ID[Action]
Event = base.Event[ID, Payload]
