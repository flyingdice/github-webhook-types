"""
    ghwht/hooks/marketplace_purchase
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains types for the 'marketplace_purchase' webhook.

    https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/webhook-events-and-payloads#marketplace_purchase
"""
import enum

from datetime import datetime
from typing import List, Optional

from pydantic import dataclasses

from . import base, common


class Action(base.Action):
    Cancelled = 'cancelled'
    Changed = 'changed'
    PendingChange = 'pending_change'
    PendingChangeCancelled = 'pending_change_cancelled'
    Purchased = 'purchased'


class BillingCycle(str, enum.Enum):
    Monthly = 'monthly'
    Yearly = 'yearly'


class PriceModel(str, enum.Enum):
    FlatRate = 'flat-rate'


@dataclasses.dataclass
class Account:
    id: int
    email: str
    login: str
    type: common.TargetType


@dataclasses.dataclass
class Plan:
    id: int
    bullets: List[str]
    name: str
    description: str
    has_free_trial: bool
    price_model: PriceModel
    monthly_price_in_cents: int
    unit_name: Optional[str]
    yearly_price_in_cents: int


@dataclasses.dataclass
class MarketplacePurchase:
    account: Account
    billing_cycle: BillingCycle
    free_trial_ends_on: Optional[datetime]
    next_billing_date: datetime
    on_free_trial: bool
    plan: Plan
    unit_count: int


@dataclasses.dataclass
class Payload(base.Payload):
    effective_date: datetime
    marketplace_purchase: MarketplacePurchase
    repository: common.Repository
    sender: common.Sender

    installation: Optional[common.Installation] = None
    organization: Optional[common.Organization] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


Name = base.EventName.MarketplacePurchase
ID = base.ID[Action]
Event = base.Event[ID, Payload]
