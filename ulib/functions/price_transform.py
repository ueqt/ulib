# pylint: skip-file
import talib


def AVGPRICE(open, high, low, close):
    ''' Average Price 平均价格

    分组: Price Transform 价格指标

    简介:

    real = AVGPRICE(open, high, low, close)
    '''
    return talib.AVGPRICE(open, high, low, close)


def MEDPRICE(high, low):
    ''' Median Price 中位数价格

    分组: Price Transform 价格指标

    简介:

    real = MEDPRICE(high, low)
    '''
    return talib.MEDPRICE(high, low)


def TYPPRICE(high, low, close):
    ''' Typical Price 代表性价格

    分组: Price Transform 价格指标

    简介:

    real = TYPPRICE(high, low, close)
    '''
    return talib.TYPPRICE(high, low, close)


def WCLPRICE(high, low, close):
    ''' Weighted Close Price 加权收盘价

    分组: Price Transform 价格指标

    简介:

    real = WCLPRICE(high, low, close)
    '''
    return talib.WCLPRICE(high, low, close)
