"""
    ghwht/hooks/security_advisory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'security_advisory' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#security_advisory
"""
import enum
from datetime import datetime
from typing import Optional, List

from pydantic import dataclasses, HttpUrl, BaseModel

from . import base


class Action(base.Action):
    Performed = 'performed'
    Published = 'published'
    Updated = 'updated'


# TODO: Need full list of severities.
class Severity(str, enum.Enum):
    High = 'high'
    Low = 'low'
    Moderate = 'moderate'


class IdentifierType(str, enum.Enum):
    CVE = 'CVE'
    GHSA = 'GHSA'


# TODO: Need full list of supported ecosystems/languages.
# https://docs.github.com/en/free-pro-team@latest/github/visualizing-repository-data-with-graphs/about-the-dependency-graph#supported-package-ecosystems
class Ecosystem(str, enum.Enum):
    Pip = 'pip'


@dataclasses.dataclass
class Identifier:
    type: IdentifierType
    value: str


@dataclasses.dataclass
class Reference:
    url: HttpUrl


@dataclasses.dataclass
class Package:
    ecosystem: str
    name: str


@dataclasses.dataclass
class PatchedVersion:
    identifier: str


@dataclasses.dataclass
class Vulnerability:
    package: Package
    severity: Severity
    vulnerable_version_range: str
    first_patched_version: PatchedVersion


class SecurityAdvisory(BaseModel):
    description: Optional[str]
    ghsa_id: str
    identifiers: List[Identifier]
    published_at: datetime
    references: List[Reference]
    summary: str
    severity: Severity
    updated_at: datetime
    vulnerabilities: List[Vulnerability]
    withdrawn_at: Optional[datetime]


@dataclasses.dataclass
class Payload(base.Payload):
    security_advisory: SecurityAdvisory


Name = base.EventName.SecurityAdvisory
ID = base.ID[Action]
Event = base.Event[ID, Payload]
