# pylint: skip-file
import talib


def HT_DCPERIOD(close):
    ''' Hilbert Transform - Dominant Cycle Period 希尔伯特变换-主导周期

    分组: Cycle Indicators 周期指标

    简介: 将价格作为信息信号，计算价格处在的周期的位置，作为择时的依据。

    real = HT_DCPERIOD(close)
    '''
    return talib.HT_DCPERIOD(close)


def HT_DCPHASE(close):
    ''' Hilbert Transform - Dominant Cycle Phase 希尔伯特变换-主导循环阶段

    分组: Cycle Indicators 周期指标

    简介:

    real = HT_DCPHASE(close)
    '''
    return talib.HT_DCPHASE(close)


def HT_PHASOR(close):
    ''' Hilbert Transform - Phasor Components 希尔伯特变换-希尔伯特变换相量分量

    分组: Cycle Indicators 周期指标

    简介:

    inphase, quadrature = HT_PHASOR(close)
    '''
    return talib.HT_PHASOR(close)


def HT_SINE(close):
    ''' Hilbert Transform - SineWave 希尔伯特变换-正弦波

    分组: Cycle Indicators 周期指标

    简介:

    sine, leadsine = HT_SINE(close)
    '''
    return talib.HT_SINE(close)


def HT_TRENDMODE(close):
    ''' Hilbert Transform - Trend vs Cycle Mode 希尔伯特变换-趋势与周期模式

    分组: Cycle Indicators 周期指标

    简介:

    integer = HT_TRENDMODE(close)
    '''
    return talib.HT_TRENDMODE(close)
