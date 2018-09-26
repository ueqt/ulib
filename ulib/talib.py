# pylint: skip-file
import talib
from .functions.overlap_studies import *
from .functions.momentum_indicator import *
from .functions.volume_indicator import *
from .volatility_indicators import *
from .price_transform import *
from .cycle_indicators import *
from .pattern_recognition import *
from .statistics_functions import *
from .math_transform import *
from .math_operators import *

# region 默认方法


def get_functions():
    '''
    Returns a list of all the functions supported by TALIB

    返回所有TALIB支持的函数列表
    '''
    return talib.get_functions()


def get_function_groups():
    '''
    Returns a dict with keys of function-group names and values of lists
    of function names ie {'group_names': ['function_names']}

    返回带分组的函数列表
    '''
    return talib.get_function_groups()

# endregion 默认方法
