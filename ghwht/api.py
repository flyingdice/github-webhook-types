"""
    ghwht/api
    ~~~~~~~~~

    Defines the public API for the `ghwht` package.
"""
from typing import Optional

from . import hooks

__all__ = ['new', 'Event', 'EventName', 'EventT', 'ID']

# Export common base types.
Event = hooks.Event
EventName = hooks.EventName
EventT = hooks.EventT
ID = hooks.ID


def new(delivery_id: str,
        event_name: str,
        hook_id: int,
        action: Optional[str],
        payload: dict) -> hooks.EventT:
    """
    Create an event instance for the given data.

    The type of Event returned is determined by the event name/action of the request.

    :param delivery_id: UUID of the delivery
    :param event_name: Name of the event
    :param hook_id: ID of the webhook
    :param action: Action of the event
    :param payload: Event data payload
    :return: Event
    """
    name = hooks.EventName(event_name)

    id_cls = hooks.NAME_TO_ID[name]
    event_cls = hooks.NAME_TO_EVENT[name]

    return event_cls(
        id=id_cls(
            event_name=name,
            action=action
        ),
        delivery_id=delivery_id,
        hook_id=hook_id,
        payload=payload
    )

