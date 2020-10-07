"""
    ghwht
    ~~~~~

    Type definitons for GitHub webhooks.
"""
from . import api, meta

new = api.new
Event = api.Event
EventName = api.EventName
EventT = api.EventT
ID = api.ID


__all__ = api.__all__
__author__ = meta.AUTHOR
__version__ = meta.VERSION
