# pylint: skip-file
import talib


def BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    ''' Bollinger Bands 布林线指标

    分组: Overlap Studies 重叠研究

    简介: 其利用统计原理，求出股价的标准差及其信赖区间，从而确定股价的波动范围及未来走势，
    利用波带显示股价的安全高低价位，因而也被称为布林带。

    分析和应用: http://www.iwencai.com/yike/detail/auid/56d0d9be66b4f7a0?rid=53

    upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    '''
    return talib.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)


def DEMA(close, timeperiod=30):
    ''' Double Exponential Moving Average 双移动平均线

    分组: Overlap Studies 重叠研究

    简介: 两条移动平均线来产生趋势信号，较长期者用来识别趋势，较短期者用来选择时机。
    正是两条平均线及价格三者的相互作用，才共同产生了趋势信号。

    分析和应用: http://www.iwencai.com/yike/detail/auid/a04d723659318237

    real = DEMA(close, timeperiod=30)
    '''
    return talib.DEMA(close, timeperiod)


def EMA(close, timeperiod=30):
    ''' Exponential Moving Average 指数平均线

    分组: Overlap Studies 重叠研究

    简介: 是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，
    并根据计算结果来进行分析，用于判断价格未来走势的变动趋势。

    分析和应用: http://www.iwencai.com/yike/detail/auid/b7a39d74783ad689?rid=589

    real = EMA(close, timeperiod=30)
    '''
    return talib.EMA(close, timeperiod)


def HT_TRENDLINE(close):
    ''' Hilbert Transform - Instantaneous Trendline 希尔伯特瞬时变换

    分组: Overlap Studies 重叠研究

    简介: 是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分析，
    用于判断价格未来走势的变动趋势。

    分析和应用: https://wenku.baidu.com/view/0e35f6eead51f01dc281f18e.html

    real = HT_TRENDLINE(close)
    '''
    return talib.HT_TRENDLINE(close)


def KAMA(close, timeperiod=30):
    ''' Kaufman Adaptive Moving Average 考夫曼的自适应移动平均线

    分组: Overlap Studies 重叠研究

    简介: 短期均线贴近价格走势，灵敏度高，但会有很多噪声，产生虚假信号；长期均线在判断趋势上一般比较准确 ，
    但是长期均线有着严重滞后的问题。我们想得到这样的均线，当价格沿一个方向快速移动时，短期的移动 平均线是最合适的；
    当价格在横盘的过程中，长期移动平均线是合适的。

    分析和应用: https://wenku.baidu.com/view/bc4bc9c59ec3d5bbfd0a7454.html?from=search

    real = KAMA(close, timeperiod=30)
    '''
    return talib.KAMA(close, timeperiod)


def MA(close, timeperiod=30, matype=0):
    ''' Moving average 移动平均线

    分组: Overlap Studies 重叠研究

    简介: 移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，
    所以一般称之为移动平均线，简称均线。
    它是将某一段时间的收盘价之和除以该周期。 比如日线MA5指5天内的收盘价除以5 。

    分析和应用: http://www.iwencai.com/yike/detail/auid/a04d723659318237?rid=96

    real = MA(close, timeperiod=30, matype=0)
    '''
    return talib.MA(close, timeperiod, matype)


def MAMA(close, fastlimit=0, slowlimit=0):
    ''' MESA Adaptive Moving Average

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
    '''
    return talib.MAMA(close, fastlimit, slowlimit)


def MAVP(close, periods, minperiod=2, maxperiod=30, matype=0):
    ''' Moving average with variable period

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
    '''
    return talib.MAVP(close, periods, minperiod, maxperiod, matype)


def MIDPOINT(close, timeperiod=14):
    ''' MidPoint over period

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = MIDPOINT(close, timeperiod=14)
    '''
    return talib.MIDPOINT(close, timeperiod)


def MIDPRICE(high, low, timeperiod=14):
    ''' Midpoint Price over period

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = MIDPRICE(high, low, timeperiod=14)
    '''
    return talib.MIDPRICE(high, low, timeperiod)


def SAR(high, low, acceleration=0, maximum=0):
    ''' Parabolic SAR 抛物线指标

    分组: Overlap Studies 重叠研究

    简介: 抛物线转向也称停损点转向，是利用抛物线方式，随时调整停损点位置以观察买卖点。
    由于停损点（又称转向点SAR）以弧形的方式移动，故称之为抛物线转向指标 。

    分析和应用: http://www.iwencai.com/yike/detail/auid/d9d94e65be7f6b5e

    real = SAR(high, low, acceleration=0, maximum=0)
    '''
    return talib.SAR(high, low, acceleration, maximum)


def SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0):
    ''' Parabolic SAR - Extended

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    '''
    return talib.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)


def SMA(close, timeperiod=30):
    ''' Simple Moving Average 简单移动平均线

    分组: Overlap Studies 重叠研究

    简介: 移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，
    所以一般称之为移动平均线，简称均线。它是将某一段时间的收盘价之和除以该周期。
    比如日线MA5指5天内的收盘价除以5 。

    分析和应用: http://www.iwencai.com/yike/detail/auid/a04d723659318237?rid=96

    real = SMA(close, timeperiod=30)
    '''
    return talib.SMA(close, timeperiod)


def T3(close, timeperiod=5, vfactor=0):
    ''' Triple Exponential Moving Average (T3) 三重指数移动平均线

    分组: Overlap Studies 重叠研究

    简介: TRIX长线操作时采用本指标的讯号，长时间按照本指标讯号交易，
    获利百分比大于损失百分比，利润相当可观。 比如日线MA5指5天内的收盘价除以5 。

    分析和应用: http://www.iwencai.com/yike/detail/auid/6c22c15ccbf24e64?rid=80

    real = T3(close, timeperiod=5, vfactor=0)
    '''
    return talib.T3(close, timeperiod, vfactor)


def TEMA(close, timeperiod=30):
    ''' Triple Exponential Moving Average

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = TEMA(close, timeperiod=30)
    '''
    return talib.TEMA(close, timeperiod)


def TRIMA(close, timeperiod=30):
    ''' Triangular Moving Average

    分组: Overlap Studies 重叠研究

    简介:

    分析和应用:

    real = TRIMA(close, timeperiod=30)
    '''
    return talib.TRIMA(close, timeperiod)


def WMA(close, timeperiod=30):
    ''' Weighted Moving Average 移动加权平均法

    分组: Overlap Studies 重叠研究

    简介: 移动加权平均法是指以每次进货的成本加上原有库存存货的成本，除以每次进货数量与原有库存存货的数量之和，
    据以计算加权平均单位成本，以此为基础计算当月发出存货的成本和期末存货的成本的一种方法。

    分析和应用: http://www.iwencai.com/yike/detail/auid/262b1dfd1c68ee30

    real = WMA(close, timeperiod=30)
    '''
    return talib.WMA(close, timeperiod)
