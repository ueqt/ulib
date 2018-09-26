# pylint: skip-file
import talib


def ADD(high, low):
    ''' Vector Arithmetic Add 向量加法运算

    分组: Math Operator 数学运算符

    简介:

    real = ADD(high, low)
    '''
    return talib.ADD(high, low)


def DIV(high, low):
    ''' Vector Arithmetic Div 向量除法运算

    分组: Math Operator 数学运算符

    简介:

    real = DIV(high, low)
    '''
    return talib.DIV(high, low)


def MAX(close, timeperiod=30):
    ''' Highest value over a specified period 周期内最大值（未满足周期返回nan)

    分组: Math Operator 数学运算符

    简介:

    real = MAX(close, timeperiod=30)
    '''
    return talib.MAX(close, timeperiod)


def MAXINDEX(close, timeperiod=30):
    ''' Index of highest value over a specified period 周期内最大值的索引

    分组: Math Operator 数学运算符

    简介:

    integer = MAXINDEX(close, timeperiod=30)
    '''
    return talib.MAXINDEX(close, timeperiod)


def MIN(close, timeperiod=30):
    ''' Lowest value over a specified period 周期内最小值 （未满足周期返回nan）

    分组: Math Operator 数学运算符

    简介:

    real = MIN(close, timeperiod=30)
    '''
    return talib.MIN(close, timeperiod)


def MININDEX(close, timeperiod=30):
    ''' Index of lowest value over a specified period 周期内最小值的索引

    分组: Math Operator 数学运算符

    简介:

    integer = MININDEX(close, timeperiod=30)
    '''
    return talib.MININDEX(close, timeperiod)


def MINMAX(close, timeperiod=30):
    ''' Lowest and highest values over a specified period 周期内最小值和最大值

    分组: Math Operator 数学运算符

    简介: (返回元组````元组（array【最小】，array【最大】）```)

    min, max = MINMAX(close, timeperiod=30)
    '''
    return talib.MINMAX(close, timeperiod)


def MINMAXINDEX(close, timeperiod=30):
    ''' Indexes of lowest and highest values over a specified period 周期内最小值和最大值索引

    分组: Math Operator 数学运算符

    简介: (返回元组````元组（array【最小】，array【最大】）```)

    minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
    '''
    return talib.MINMAXINDEX(close, timeperiod)


def MULT(high, low):
    ''' Vector Arithmetic Mult 向量乘法运算

    分组: Math Operator 数学运算符

    简介:

    real = MULT(high, low)
    '''
    return talib.MULT(high, low)


def SUB(high, low):
    ''' Vector Arithmetic Substraction 向量减法运算

    分组: Math Operator 数学运算符

    简介:

    real = SUB(high, low)
    '''
    return talib.SUB(high, low)


def SUM(close, timeperiod=30):
    ''' Summation 周期内求和

    分组: Math Operator 数学运算符

    简介:

    real = SUM(close, timeperiod=30)
    '''
    return talib.SUM(close, timeperiod)
