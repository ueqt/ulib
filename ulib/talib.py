# pylint: skip-file
import talib
from .functions.overlap_studies import *
from .functions.momentum_indicator import *
from .functions.volume_indicators import *
from .functions.volatility_indicators import *
from .functions.price_transform import *
from .functions.cycle_indicators import *
from .functions.pattern_recognition import *
from .functions.statistic_functions import *
from .functions.math_transform import *
from .functions.math_operators import *

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
