# pylint: skip-file
import talib


def BETA(high, low, timeperiod=5):
    ''' Beta β系数也称为贝塔系数

    分组: Statistic Functions 统计函数

    简介: 一种风险指数，用来衡量个别股票或 股票基金相对于整个股市的价格波动情况
    贝塔系数衡量股票收益相对于业绩评价基准收益的总体波动性，是一个相对指标。
    β 越高，意味着股票相对于业绩评价基准的波动性越大。
    β 大于 1 ， 则股票的波动性大于业绩评价基准的波动性。反之亦然。 用途：
1）计算资本成本，做出投资决策（只有回报率高于资本成本的项目才应投资）；
2）计算资本成本，制定业绩考核及激励标准；
3）计算资本成本，进行资产估值（Beta是现金流贴现模型的基础）；
4）确定单个资产或组合的系统风险，用于资产组合的投资管理，特别是股指期货或其他金融衍生品的避险（或投机）

    real = BETA(high, low, timeperiod=5)
    '''
    return talib.BETA(high, low, timeperiod)


def CORREL(high, low, timeperiod=30):
    ''' Pearson's Correlation Coefficient (r) 皮尔逊相关系数

    分组: Statistic Functions 统计函数

    简介: 用于度量两个变量X和Y之间的相关（线性相关），其值介于-1与1之间
皮尔逊相关系数是一种度量两个变量间相关程度的方法。它是一个介于 1 和 -1 之间的值，
其中，1 表示变量完全正相关， 0 表示无关，-1 表示完全负相关。

    real = CORREL(high, low, timeperiod=30)
    '''
    return talib.CORREL(high, low, timeperiod)


def LINEARREG(close, timeperiod=14):
    ''' Linear Regression 线性回归

    分组: Statistic Functions 统计函数

    简介:

    real = LINEARREG(close, timeperiod=14)
    '''
    return talib.LINEARREG(close, timeperiod)


def LINEARREG_ANGLE(close, timeperiod=14):
    ''' Linear Regression Angle 线性回归的角度

    分组: Statistic Functions 统计函数

    简介:

    real = LINEARREG_ANGLE(close, timeperiod=14)
    '''
    return talib.LINEARREG_ANGLE(close, timeperiod)


def LINEARREG_INTERCEPT(close, timeperiod=14):
    ''' Linear Regression Intercept 线性回归截距

    分组: Statistic Functions 统计函数

    简介:

    real = LINEARREG_INTERCEPT(close, timeperiod=14)
    '''
    return talib.LINEARREG_INTERCEPT(close, timeperiod)


def LINEARREG_SLOPE(close, timeperiod=14):
    ''' Linear Regression Slope 线性回归斜率指标

    分组: Statistic Functions 统计函数

    简介:

    real = LINEARREG_SLOPE(close, timeperiod=14)
    '''
    return talib.LINEARREG_SLOPE(close, timeperiod)


def STDDEV(close, timeperiod=5, nbdev=1):
    ''' Standard Deviation 标准偏差

    分组: Statistic Functions 统计函数

    简介: 种量度数据分布的分散程度之标准，用以衡量数据值偏离算术平均值的程度。
    标准偏差越小，这些值偏离平均值就越少，反之亦然。
    标准偏差的大小可通过标准偏差与平均值的倍率关系来衡量。

    real = STDDEV(close, timeperiod=5, nbdev=1)
    '''
    return talib.STDDEV(close, timeperiod, nbdev)


def TSF(close, timeperiod=14):
    ''' Time Series Forecast 时间序列预测

    分组: Statistic Functions 统计函数

    简介: 一种历史资料延伸预测，也称历史引伸预测法。
    是以时间数列所能反映的社会经济现象的发展过程和规律性，
    进行引伸外推，预测其发展趋势的方法

    real = TSF(close, timeperiod=14)
    '''
    return talib.TSF(close, timeperiod)


def VAR(close, timeperiod=5, nbdev=1):
    ''' VAR 方差

    分组: Statistic Functions 统计函数

    简介: 方差用来计算每一个变量（观察值）与总体均数之间的差异。
    为避免出现离均差总和为零，离均差平方和受样本含量的影响，
    统计学采用平均离均差平方和来描述变量的变异程度

    real = VAR(close, timeperiod=5, nbdev=1)
    '''
    return talib.VAR(close, timeperiod, nbdev)
