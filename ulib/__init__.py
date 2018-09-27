import pkgutil

__title__ = 'ulib'
__author__ = 'ueqt'
__description__ = 'stock base library'
__version__ = pkgutil.get_data(
    __package__, 'VERSION.txt').decode('utf8').strip()
__cake__ = u'\u2778 \U0001f370 \u2728'

del pkgutil

# pylint: disable=W0401
from .talib import *
