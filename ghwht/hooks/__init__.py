"""
    ghwht/hooks
    ~~~~~~~~~~~

    Contains modules for each type of webhook event.
"""
from typing import Dict, Type

from . import base, check_run, installation, ping

__all__ = ['NAME_TO_EVENT', 'Event', 'EventName', 'EventT', 'ID']

# Alias to simplify imports.
Event = base.Event
EventName = base.EventName
EventT = base.EventT
ID = base.ID
IDT = base.IDT


def hooks_modules():
    """
    Generator function that yields all registered webhook event modules.
    """
    yield from (check_run, installation, ping)


# Lookup table that maps event names to their appropriate identifier type.
# Ex: 'issues' -> ghwht.hooks.issues.Identifier.
NAME_TO_ID: Dict[EventName, Type[IDT]] = dict(
    (module.Name, module.ID)
    for module in hooks_modules()
)


# Lookup table that maps event names to their appropriate type.
# Ex: 'issues' -> ghwht.hooks.issues.Event.
NAME_TO_EVENT: Dict[EventName, Type[EventT]] = dict(
    (module.Name, module.Event)
    for module in hooks_modules()
)
