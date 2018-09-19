# pylint: skip-file
import talib
from .functions.overlap_studies import *
from .functions.momentum_indicator import *

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

# 'Cycle Indicators': [
#         'HT_DCPERIOD',
#         'HT_DCPHASE',
#         'HT_PHASOR',
#         'HT_SINE',
#         'HT_TRENDMODE',
#         ],
#     'Math Operators': [
#         'ADD',
#         'DIV',
#         'MAX',
#         'MAXINDEX',
#         'MIN',
#         'MININDEX',
#         'MINMAX',
#         'MINMAXINDEX',
#         'MULT',
#         'SUB',
#         'SUM',
#         ],
#     'Math Transform': [
#         'ACOS',
#         'ASIN',
#         'ATAN',
#         'CEIL',
#         'COS',
#         'COSH',
#         'EXP',
#         'FLOOR',
#         'LN',
#         'LOG10',
#         'SIN',
#         'SINH',
#         'SQRT',
#         'TAN',
#         'TANH',
#         ],

#     'Pattern Recognition': [
#         'CDL2CROWS',
#         'CDL3BLACKCROWS',
#         'CDL3INSIDE',
#         'CDL3LINESTRIKE',
#         'CDL3OUTSIDE',
#         'CDL3STARSINSOUTH',
#         'CDL3WHITESOLDIERS',
#         'CDLABANDONEDBABY',
#         'CDLADVANCEBLOCK',
#         'CDLBELTHOLD',
#         'CDLBREAKAWAY',
#         'CDLCLOSINGMARUBOZU',
#         'CDLCONCEALBABYSWALL',
#         'CDLCOUNTERATTACK',
#         'CDLDARKCLOUDCOVER',
#         'CDLDOJI',
#         'CDLDOJISTAR',
#         'CDLDRAGONFLYDOJI',
#         'CDLENGULFING',
#         'CDLEVENINGDOJISTAR',
#         'CDLEVENINGSTAR',
#         'CDLGAPSIDESIDEWHITE',
#         'CDLGRAVESTONEDOJI',
#         'CDLHAMMER',
#         'CDLHANGINGMAN',
#         'CDLHARAMI',
#         'CDLHARAMICROSS',
#         'CDLHIGHWAVE',
#         'CDLHIKKAKE',
#         'CDLHIKKAKEMOD',
#         'CDLHOMINGPIGEON',
#         'CDLIDENTICAL3CROWS',
#         'CDLINNECK',
#         'CDLINVERTEDHAMMER',
#         'CDLKICKING',
#         'CDLKICKINGBYLENGTH',
#         'CDLLADDERBOTTOM',
#         'CDLLONGLEGGEDDOJI',
#         'CDLLONGLINE',
#         'CDLMARUBOZU',
#         'CDLMATCHINGLOW',
#         'CDLMATHOLD',
#         'CDLMORNINGDOJISTAR',
#         'CDLMORNINGSTAR',
#         'CDLONNECK',
#         'CDLPIERCING',
#         'CDLRICKSHAWMAN',
#         'CDLRISEFALL3METHODS',
#         'CDLSEPARATINGLINES',
#         'CDLSHOOTINGSTAR',
#         'CDLSHORTLINE',
#         'CDLSPINNINGTOP',
#         'CDLSTALLEDPATTERN',
#         'CDLSTICKSANDWICH',
#         'CDLTAKURI',
#         'CDLTASUKIGAP',
#         'CDLTHRUSTING',
#         'CDLTRISTAR',
#         'CDLUNIQUE3RIVER',
#         'CDLUPSIDEGAP2CROWS',
#         'CDLXSIDEGAP3METHODS',
#         ],
#     'Price Transform': [
#         'AVGPRICE',
#         'MEDPRICE',
#         'TYPPRICE',
#         'WCLPRICE',
#         ],
#     'Statistic Functions': [
#         'BETA',
#         'CORREL',
#         'LINEARREG',
#         'LINEARREG_ANGLE',
#         'LINEARREG_INTERCEPT',
#         'LINEARREG_SLOPE',
#         'STDDEV',
#         'TSF',
#         'VAR',
#         ],
#     'Volatility Indicators': [
#         'ATR',
#         'NATR',
#         'TRANGE',
#         ],
#     'Volume Indicators': [
#         'AD',
#         'ADOSC',
#         'OBV'
#         ],
