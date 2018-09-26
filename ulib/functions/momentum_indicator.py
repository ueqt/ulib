# pylint: skip-file
import talib


def ADX(high, low, close, timeperiod=14):
    ''' Average Directional Movement Index 平均趋向指数

    分组: Momentum Indicator 动量指标

    简介: 使用ADX指标，指标判断盘整、振荡和单边趋势。

    real = ADX(high, low, close, timeperiod=14)
    '''
    return talib.ADX(high, low, close, timeperiod)


def ADXR(high, low, close, timeperiod=14):
    ''' Average Directional Movement Index Rating 平均趋向指数的趋向指数

    分组: Momentum Indicator 动量指标

    简介: 使用ADXR指标，指标判断ADX趋势。

    real = ADXR(high, low, close, timeperiod=14)
    '''
    return talib.ADXR(high, low, close, timeperiod)


def APO(close, fastperiod=12, slowperiod=26, matype=0):
    '''  Absolute Price Oscillator

    分组: Momentum Indicator 动量指标

    简介:

    real = APO(close, fastperiod=12, slowperiod=26, matype=0)
    '''
    return talib.APO(close, fastperiod, slowperiod, matype)


def AROON(high, low, timeperiod=14):
    ''' Aroon 阿隆指标

    分组: Momentum Indicator 动量指标

    简介: 该指标是通过计算自价格达到近期最高值和最低值以来所经过的期间数，
    阿隆指标帮助你预测价格趋势到趋势区域（或者反过来，从趋势区域到趋势）的变化。

    aroondown, aroonup = AROON(high, low, timeperiod=14)
    '''
    return talib.AROON(high, low, timeperiod)


def AROONOSC(high, low, timeperiod=14):
    ''' Aroon Oscillator 阿隆振荡

    分组: Momentum Indicator 动量指标

    简介:

    real = AROONOSC(high, low, timeperiod=14)
    '''
    return talib.AROONOSC(high, low, timeperiod=14)


def BOP(open, high, low, close):
    ''' Balance Of Power 均势

    分组: Momentum Indicator 动量指标

    简介:

    real = BOP(open, high, low, close)
    '''
    return talib.BOP(open, high, low, close)


def CCI(high, low, close, timeperiod=14):
    ''' Commodity Channel Index 顺势指标

    分组: Momentum Indicator 动量指标

    简介: CCI指标专门测量股价是否已超出常态分布范围

    real = CCI(high, low, close, timeperiod=14)
    '''
    return talib.CCI(high, low, close, timeperiod)


def CMO(close, timeperiod=14):
    ''' Chande Momentum Oscillator 钱德动量摆动指标

    分组: Momentum Indicator 动量指标

    简介: 与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，
    钱德动量指标在计算公式的分子中采用上涨日和下跌日的数据。 计算公式：CMO=（Su－Sd）*100/（Su+Sd）
    其中：Su是今日收盘价与昨日收盘价（上涨日）差值加总。若当日下跌，则增加值为0；
    Sd是今日收盘价与做日收盘价（下跌日）差值的绝对值加总。若当日上涨，则增加值为0；

    real = CMO(close, timeperiod=14)
    '''
    return talib.CMO(close, timeperiod)


def DX(high, low, close, timeperiod=14):
    ''' Directional Movement Index DMI指标又叫动向指标或趋向指标

    分组: Momentum Indicator 动量指标

    简介: 通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，
    即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，
    从而提供对趋势判断依据的一种技术指标。

    real = DX(high, low, close, timeperiod=14)
    '''
    return talib.DX(high, low, close, timeperiod)


def MACD(close, fastperiod=12, slowperiod=26, signalperiod=9):
    ''' Moving Average Convergence/Divergence 平滑异同移动平均线

    分组: Momentum Indicator 动量指标

    简介: 利用收盘价的短期（常用为12日）指数移动平均线与长期（常用为26日）指数移动平均线之间的聚合与分离状况，
    对买进、卖出时机作出研判的技术指标。

    macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    '''
    return talib.MACD(close, fastperiod, slowperiod, signalperiod)


def MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
    ''' MACD with controllable MA type

    分组: Momentum Indicator 动量指标

    简介:

    macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
    '''
    return talib.MACDEXT(close, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod, signalmatype)


def MACDFIX(close, signalperiod=9):
    ''' Moving Average Convergence/Divergence Fix 12/26

    分组: Momentum Indicator 动量指标

    简介:

    macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)
    '''
    return talib.MACDFIX(close, signalperiod)


def MFI(high, low, close, volume, timeperiod=14):
    ''' Money Flow Index 资金流量指标

    分组: Momentum Indicator 动量指标

    简介: 属于量价类指标，反映市场的运行趋势

    real = MFI(high, low, close, volume, timeperiod=14)
    '''
    return talib.MFI(high, low, close, volume, timeperiod)


def MINUS_DI(high, low, close, timeperiod=14):
    ''' Minus Directional Indicator 下升动向值

    分组: Momentum Indicator 动量指标

    简介: 通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，
    即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，
    从而提供对趋势判断依据的一种技术指标。

    real = MINUS_DI(high, low, close, timeperiod=14)
    '''
    return talib.MINUS_DI(high, low, close, timeperiod)


def MINUS_DM(high, low, timeperiod=14):
    ''' Minus Directional Movement 上升动向值

    分组: Momentum Indicator 动量指标

    简介: 通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，
    即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，
    从而提供对趋势判断依据的一种技术指标。

    real = MINUS_DM(high, low, timeperiod=14)
    '''
    return talib.MINUS_DM(high, low, timeperiod)


def MOM(close, timeperiod=10):
    ''' Momentum 动量

    分组: Momentum Indicator 动量指标

    简介: 投资学中意思为续航，指股票(或经济指数)持续增长的能力。
    研究发现，赢家组合在牛市中存在着正的动量效应，输家组合在熊市中存在着负的动量效应。

    real = MOM(close, timeperiod=10)
    '''
    return talib.MOM(close, timeperiod)


def PLUS_DI(high, low, close, timeperiod=14):
    ''' Plus Directional Indicator

    分组: Momentum Indicator 动量指标

    简介:

    real = PLUS_DI(high, low, close, timeperiod=14)
    '''
    return talib.PLUS_DI(high, low, close, timeperiod)


def PLUS_DM(high, low, timeperiod=14):
    ''' Plus Directional Movement

    分组: Momentum Indicator 动量指标

    简介:

    real = PLUS_DM(high, low, timeperiod=14)
    '''
    return talib.PLUS_DM(high, low, timeperiod)


def PPO(close, fastperiod=12, slowperiod=26, matype=0):
    ''' Percentage Price Oscillator 价格震荡百分比指数

    分组: Momentum Indicator 动量指标

    简介: 价格震荡百分比指标（PPO）是一个和MACD指标非常接近的指标。
    PPO标准设定和MACD设定非常相似：12,26,9和PPO，
    和MACD一样说明了两条移动平均线的差距，
    但是它们有一个差别是PPO是用百分比说明。

    real = PPO(close, fastperiod=12, slowperiod=26, matype=0)
    '''
    return talib.PPO(close, fastperiod, slowperiod, matype)


def ROC(close, timeperiod=10):
    ''' Rate of change 变动率指标

    分组: Momentum Indicator 动量指标

    简介: ROC是由当天的股价与一定的天数之前的某一天股价比较，
    其变动速度的大小,来反映股票市变动的快慢程度
    ((price/prevPrice)-1)*100

    real = ROC(close, timeperiod=10)
    '''
    return talib.ROC(close, timeperiod)


def ROCP(close, timeperiod=10):
    ''' Rate of change Percentage

    分组: Momentum Indicator 动量指标

    简介: (price-prevPrice)/prevPrice

    real = ROCP(close, timeperiod=10)
    '''
    return talib.ROCP(close, timeperiod)


def ROCR(close, timeperiod=10):
    ''' Rate of change ratio

    分组: Momentum Indicator 动量指标

    简介: (price/prevPrice)

    real = ROCR(close, timeperiod=10)
    '''
    return talib.ROCR(close, timeperiod)


def ROCR100(close, timeperiod=10):
    ''' Rate of change ratio 100 scale

    分组: Momentum Indicator 动量指标

    简介: (price/prevPrice)*100

    real = ROCR100(close, timeperiod=10)
    '''
    return talib.ROCR100(close, timeperiod)


def RSI(close, timeperiod=14):
    ''' Relative Strength Index 相对强弱指数

    分组: Momentum Indicator 动量指标

    简介: 是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。

    real = RSI(close, timeperiod=14)
    '''
    return talib.RSI(close, timeperiod)


def STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    ''' Stochastic 随机指标,俗称KD

    分组: Momentum Indicator 动量指标

    简介: 随机指标,俗称KD

    slowk, slowd = STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    '''
    return talib.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)


def STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0):
    ''' Stochastic Fast

    分组: Momentum Indicator 动量指标

    简介:

    fastk, fastd = STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    '''
    return talib.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)


def STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    ''' Stochastic Relative Strength Index

    分组: Momentum Indicator 动量指标

    简介:

    fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    '''
    return talib.STOCHRSI(close, timeperiod, fastk_period, fastd_period, fastd_matype)


def TRIX(close, timeperiod=30):
    ''' 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA

    分组: Momentum Indicator 动量指标

    简介:

    real = TRIX(close, timeperiod=30)
    '''
    return talib.TRIX(close, timeperiod)


def ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    ''' Ultimate Oscillator 终极波动指标

    分组: Momentum Indicator 动量指标

    简介: UOS是一种多方位功能的指标，除了趋势确认及超买超卖方面的作用之外，
    它的“突破”讯号不仅可以提供最适当的交易时机之外，更可以进一步加强指标的可靠度。

    real = ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    '''
    return talib.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)


def WILLR(high, low, close, timeperiod=14):
    ''' Williams' %R 威廉指标

    分组: Momentum Indicator 动量指标

    简介: WMS表示的是市场处于超买还是超卖状态。
    股票投资分析方法主要有如下三种：基本分析、技术分析、演化分析。
    在实际应用中，它们既相互联系，又有重要区别。

    real = WILLR(high, low, close, timeperiod=14)
    '''
    return talib.WILLR(high, low, close, timeperiod)
