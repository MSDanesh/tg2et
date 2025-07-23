from pyeitaa.client import Client
from .methods import Methods
from .utils import Utils


class EitaaManager(Client, Methods, Utils): ...