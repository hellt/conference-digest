from .usenix import UsenixFetcher
from .ietf import IetfFetcher
from .sched import SchedFetcher
from .sigcomm import SigcommFetcher
from .netdev import NetdevFetcher
from .nanog import NanogFetcher
from .autocon import AutoconFetcher
from .ovscon import OvsconFetcher
from .ciscolive import CiscoLiveFetcher

FETCHERS = {
    "usenix": UsenixFetcher(),
    "ietf": IetfFetcher(),
    "sched": SchedFetcher(),
    "sigcomm": SigcommFetcher(),
    "netdev": NetdevFetcher(),
    "nanog": NanogFetcher(),
    "autocon": AutoconFetcher(),
    "ovscon": OvsconFetcher(),
    "ciscolive": CiscoLiveFetcher(),
}


def get_fetcher(name: str):
    if name not in FETCHERS:
        raise KeyError(f"unknown fetcher '{name}'; known: {sorted(FETCHERS)}")
    return FETCHERS[name]
