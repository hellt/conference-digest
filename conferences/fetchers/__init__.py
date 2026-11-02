from .usenix import UsenixFetcher
from .ietf import IetfFetcher
from .sched import SchedFetcher
from .sigcomm import SigcommFetcher
from .netdev import NetdevFetcher
from .nanog import NanogFetcher
from .autocon import AutoconFetcher
from .ovscon import OvsconFetcher
from .ciscolive import CiscoLiveFetcher
from .ripe import RipeFetcher
from .nlnog import NlnogFetcher
from .denog import DenogFetcher
from .gtc import GtcFetcher
from .ccs import CcsFetcher
from .imc import ImcFetcher
from .conext import ConextFetcher
from .apricot import ApricotFetcher
from .fosdem import FosdemFetcher
from .pretalx import PretalxFetcher
from .imc import ImcFetcher
from .conext import ConextFetcher
from .apricot import ApricotFetcher
from .fosdem import FosdemFetcher
from .pretalx import PretalxFetcher

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
    "ripe": RipeFetcher(),
    "nlnog": NlnogFetcher(),
    "denog": DenogFetcher(),
    "gtc": GtcFetcher(),
    "ccs": CcsFetcher(),
    "imc": ImcFetcher(),
    "conext": ConextFetcher(),
    "apricot": ApricotFetcher(),
    "fosdem": FosdemFetcher(),
    "pretalx": PretalxFetcher(),
}


def get_fetcher(name: str):
    if name not in FETCHERS:
        raise KeyError(f"unknown fetcher '{name}'; known: {sorted(FETCHERS)}")
    return FETCHERS[name]
