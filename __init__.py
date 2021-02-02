"""
A high level api used to connect to [the travelers](https://thetravelers.online) from python. Use the readme to get installation directions.\n
Links: 
	PyPi - https://pypi.org/project/thetravelers.online-Api/
	Github - https://github.com/LightningWB
"""
from .types import gameObject
from .travelerApi import travelerApi
from .lowApi import lowClient as baseClient
from .world import deriveTile as generateTileAt
from .world import getPerlin
from .world import isTileEvent

if __name__=='__init__':
    pass