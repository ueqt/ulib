# pylint: skip-file
import talib


def CDL2CROWS(open, high, low, close):
    ''' Two Crows 两只乌鸦

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴，
    收盘比前一日收盘价低，预示股价下跌。

    integer = CDL2CROWS(open, high, low, close)
    '''
    return talib.CDL2CROWS(open, high, low, close)


def CDL3BLACKCROWS(open, high, low, close):
    ''' Three Black Crows 三只乌鸦

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价，
    每日开盘价都在上根K线实体内，预示股价下跌。

    integer = CDL3BLACKCROWS(open, high, low, close)
    '''
    return talib.CDL3BLACKCROWS(open, high, low, close)


def CDL3INSIDE(open, high, low, close):
    ''' Three Inside Up/Down 三内部上涨和下跌

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，母子信号+长K线，以三内部上涨为例，K线为阴阳阳，
    第三天收盘价高于第一天开盘价，第二天K线在第一天K线内部，预示着股价上涨。

    integer = CDL3INSIDE(open, high, low, close)
    '''
    return talib.CDL3INSIDE(open, high, low, close)


def CDL3LINESTRIKE(open, high, low, close):
    ''' Three-Line Strike 三线打击

    分组: Pattern Recognition 形态识别

    简介: 四日K线模式，前三根阳线，每日收盘价都比前一日高，
    开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。

    integer = CDL3LINESTRIKE(open, high, low, close)
    '''
    return talib.CDL3LINESTRIKE(open, high, low, close)


def CDL3OUTSIDE(open, high, low, close):
    ''' Three Outside Up/Down 三外部上涨和下跌

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，与三内部上涨和下跌类似，K线为阴阳阳，但第一日与第二日的K线形态相反，
    以三外部上涨为例，第一日K线在第二日K线内部，预示着股价上涨。

    integer = CDL3OUTSIDE(open, high, low, close)
    '''
    return talib.CDL3OUTSIDE(open, high, low, close)


def CDL3STARSINSOUTH(open, high, low, close):
    ''' Three Stars In The South 南方三星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，与大敌当前相反，三日K线皆阴，第一日有长下影线，
    第二日与第一日类似，K线整体小于第一日，第三日无下影线实体信号，
    成交价格都在第一日振幅之内，预示下跌趋势反转，股价上升。

    integer = CDL3STARSINSOUTH(open, high, low, close)
    '''
    return talib.CDL3STARSINSOUTH(open, high, low, close)


def CDL3WHITESOLDIERS(open, high, low, close):
    ''' Three Advancing White Soldiers 三个白兵

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，三日K线皆阳， 每日收盘价变高且接近最高价，
    开盘价在前一日实体上半部，预示股价上升。

    integer = CDL3WHITESOLDIERS(open, high, low, close)
    '''
    return talib.CDL3WHITESOLDIERS(open, high, low, close)


def CDLABANDONEDBABY(open, high, low, close, penetration=0):
    ''' Abandoned Baby 弃婴

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，第二日价格跳空且收十字星（开盘价与收盘价接近， 最高价最低价相差不大），
    预示趋势反转，发生在顶部下跌，底部上涨。

    integer = CDLABANDONEDBABY(open, high, low, close, penetration=0)
    '''
    return talib.CDLABANDONEDBABY(open, high, low, close, penetration)


def CDLADVANCEBLOCK(open, high, low, close):
    ''' Advance Block 大敌当前

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，三日都收阳，每日收盘价都比前一日高，
    开盘价都在前一日实体以内，实体变短，上影线变长。

    integer = CDLADVANCEBLOCK(open, high, low, close)
    '''
    return talib.CDLADVANCEBLOCK(open, high, low, close)


def CDLBELTHOLD(open, high, low, close):
    ''' Belt-hold 捉腰带线

    分组: Pattern Recognition 形态识别

    简介: 两日K线模式，下跌趋势中，第一日阴线，
    第二日开盘价为最低价，阳线，收盘价接近最高价，预示价格上涨。

    integer = CDLBELTHOLD(open, high, low, close)
    '''
    return talib.CDLBELTHOLD(open, high, low, close)


def CDLBREAKAWAY(open, high, low, close):
    ''' Breakaway 脱离

    分组: Pattern Recognition 形态识别

    简介: 五日K线模式，以看涨脱离为例，下跌趋势中，第一日长阴线，
    第二日跳空阴线，延续趋势开始震荡， 第五日长阳线，
    收盘价在第一天收盘价与第二天开盘价之间，预示价格上涨。

    integer = CDLBREAKAWAY(open, high, low, close)
    '''
    return talib.CDLBREAKAWAY(open, high, low, close)


def CDLCLOSINGMARUBOZU(open, high, low, close):
    ''' Closing Marubozu 收盘缺影线

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，以阳线为例，最低价低于开盘价，
    收盘价等于最高价，预示着趋势持续。

    integer = CDLCLOSINGMARUBOZU(open, high, low, close)
    '''
    return talib.CDLCLOSINGMARUBOZU(open, high, low, close)


def CDLCONCEALBABYSWALL(open, high, low, close):
    ''' Concealing Baby Swallow 藏婴吞没

    分组: Pattern Recognition 形态识别

    简介: 四日K线模式，下跌趋势中，前两日阴线无影线 ，
    第二日开盘、收盘价皆低于第二日，第三日倒锤头，
    第四日开盘价高于前一日最高价，收盘价低于前一日最低价，预示着底部反转。

    integer = CDLCONCEALBABYSWALL(open, high, low, close)
    '''
    return talib.CDLCONCEALBABYSWALL(open, high, low, close)


def CDLCOUNTERATTACK(open, high, low, close):
    ''' Counterattack 反击线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与分离线类似。

    integer = CDLCOUNTERATTACK(open, high, low, close)
    '''
    return talib.CDLCOUNTERATTACK(open, high, low, close)


def CDLDARKCLOUDCOVER(open, high, low, close, penetration=0):
    ''' Dark Cloud Cover 乌云压顶

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，第一日长阳，第二日开盘价高于前一日最高价，
    收盘价处于前一日实体中部以下，预示着股价下跌。

    integer = CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
    '''
    return talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration)


def CDLDOJI(open, high, low, close):
    ''' Doji 十字

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，开盘价与收盘价基本相同。

    integer = CDLDOJI(open, high, low, close)
    '''
    return talib.CDLDOJI(open, high, low, close)


def CDLDOJISTAR(open, high, low, close):
    ''' Doji Star 十字星

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，开盘价与收盘价基本相同，
    上下影线不会很长，预示着当前趋势反转。

    integer = CDLDOJISTAR(open, high, low, close)
    '''
    return talib.CDLDOJISTAR(open, high, low, close)


def CDLDRAGONFLYDOJI(open, high, low, close):
    ''' Dragonfly Doji 蜻蜓十字/T形十字

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，开盘后价格一路走低，
    之后收复，收盘价与开盘价相同，预示趋势反转。

    integer = CDLDRAGONFLYDOJI(open, high, low, close)
    '''
    return talib.CDLDRAGONFLYDOJI(open, high, low, close)


def CDLENGULFING(open, high, low, close):
    ''' Engulfing Pattern 吞噬模式

    分组: Pattern Recognition 形态识别

    简介: 两日K线模式，分多头吞噬和空头吞噬，以多头吞噬为例，
    第一日为阴线， 第二日阳线，第一日的开盘价和收盘价在第二日开盘价收盘价之内，但不能完全相同。

    integer = CDLENGULFING(open, high, low, close)
    '''
    return talib.CDLENGULFING(open, high, low, close)


def CDLEVENINGDOJISTAR(open, high, low, close, penetration=0):
    ''' Evening Doji Star 十字暮星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，基本模式为暮星，第二日收盘价和开盘价相同，预示顶部反转。

    integer = CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
    '''
    return talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration)


def CDLEVENINGSTAR(open, high, low, close, penetration=0):
    ''' Evening Star 暮星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，与晨星相反，上升趋势中, 第一日阳线，第二日价格振幅较小，第三日阴线，预示顶部反转。

    integer = CDLEVENINGSTAR(open, high, low, close, penetration=0)
    '''
    return talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)


def CDLGAPSIDESIDEWHITE(open, high, low, close):
    ''' Up/Down-gap side-by-side white lines 向上/下跳空并列阳线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，上升趋势向上跳空，下跌趋势向下跳空,
    第一日与第二日有相同开盘价，实体长度差不多，则趋势持续。

    integer = CDLGAPSIDESIDEWHITE(open, high, low, close)
    '''
    return talib.CDLGAPSIDESIDEWHITE(open, high, low, close)


def CDLGRAVESTONEDOJI(open, high, low, close):
    ''' Gravestone Doji 墓碑十字/倒T十字

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，开盘价与收盘价相同，上影线长，无下影线，预示底部反转。

    integer = CDLGRAVESTONEDOJI(open, high, low, close)
    '''
    return talib.CDLGRAVESTONEDOJI(open, high, low, close)


def CDLHAMMER(open, high, low, close):
    ''' Hammer 锤头

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，实体较短，无上影线，
    下影线大于实体长度两倍，处于下跌趋势底部，预示反转。

    integer = CDLHAMMER(open, high, low, close)
    '''
    return talib.CDLHAMMER(open, high, low, close)


def CDLHANGINGMAN(open, high, low, close):
    ''' Hanging Man 上吊线

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，形状与锤子类似，处于上升趋势的顶部，预示着趋势反转。

    integer = CDLHANGINGMAN(open, high, low, close)
    '''
    return talib.CDLHANGINGMAN(open, high, low, close)


def CDLHARAMI(open, high, low, close):
    ''' Harami Pattern 母子线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，分多头母子与空头母子，两者相反，以多头母子为例，在下跌趋势中，第一日K线长阴，
    第二日开盘价收盘价在第一日价格振幅之内，为阳线，预示趋势反转，股价上升。

    integer = CDLHARAMI(open, high, low, close)
    '''
    return talib.CDLHARAMI(open, high, low, close)


def CDLHARAMICROSS(open, high, low, close):
    ''' Harami Cross Pattern 十字孕线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与母子县类似，若第二日K线是十字线，
    便称为十字孕线，预示着趋势反转。

    integer = CDLHARAMICROSS(open, high, low, close)
    '''
    return talib.CDLHARAMICROSS(open, high, low, close)


def CDLHIGHWAVE(open, high, low, close):
    ''' High-Wave Candle 风高浪大线

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，具有极长的上/下影线与短的实体，预示着趋势反转。

    integer = CDLHIGHWAVE(open, high, low, close)
    '''
    return talib.CDLHIGHWAVE(open, high, low, close)


def CDLHIKKAKE(open, high, low, close):
    ''' Hikkake Pattern 陷阱

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，与母子类似，第二日价格在前一日实体范围内,
    第三日收盘价高于前两日，反转失败，趋势继续。

    integer = CDLHIKKAKE(open, high, low, close)
    '''
    return talib.CDLHIKKAKE(open, high, low, close)


def CDLHIKKAKEMOD(open, high, low, close):
    ''' Modified Hikkake Pattern 修正陷阱

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，与陷阱类似，上升趋势中，第三日跳空高开；
    下跌趋势中，第三日跳空低开，反转失败，趋势继续。

    integer = CDLHIKKAKEMOD(open, high, low, close)
    '''
    return talib.CDLHIKKAKEMOD(open, high, low, close)


def CDLHOMINGPIGEON(open, high, low, close):
    ''' Homing Pigeon 家鸽

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与母子线类似，不同的的是二日K线颜色相同，
    第二日最高价、最低价都在第一日实体之内，预示着趋势反转。

    integer = CDLHOMINGPIGEON(open, high, low, close)
    '''
    return talib.CDLHOMINGPIGEON(open, high, low, close)


def CDLIDENTICAL3CROWS(open, high, low, close):
    ''' Identical Three Crows 三胞胎乌鸦

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，上涨趋势中，三日都为阴线，长度大致相等，
    每日开盘价等于前一日收盘价，收盘价接近当日最低价，预示价格下跌。

    integer = CDLIDENTICAL3CROWS(open, high, low, close)
    '''
    return talib.CDLIDENTICAL3CROWS(open, high, low, close)


def CDLINNECK(open, high, low, close):
    ''' In-Neck Pattern 颈内线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，下跌趋势中，第一日长阴线， 第二日开盘价较低，
    收盘价略高于第一日收盘价，阳线，实体较短，预示着下跌继续。

    integer = CDLINNECK(open, high, low, close)
    '''
    return talib.CDLINNECK(open, high, low, close)


def CDLINVERTEDHAMMER(open, high, low, close):
    ''' Inverted Hammer 倒锤头

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，上影线较长，长度为实体2倍以上，
    无下影线，在下跌趋势底部，预示着趋势反转。

    integer = CDLINVERTEDHAMMER(open, high, low, close)
    '''
    return talib.CDLINVERTEDHAMMER(open, high, low, close)


def CDLKICKING(open, high, low, close):
    ''' Kicking 反冲形态

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与分离线类似，两日K线为秃线，颜色相反，存在跳空缺口。

    integer = CDLKICKING(open, high, low, close)
    '''
    return talib.CDLKICKING(open, high, low, close)


def CDLKICKINGBYLENGTH(open, high, low, close):
    ''' Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与反冲形态类似，较长缺影线决定价格的涨跌。

    integer = CDLKICKINGBYLENGTH(open, high, low, close)
    '''
    return talib.CDLKICKINGBYLENGTH(open, high, low, close)


def CDLLADDERBOTTOM(open, high, low, close):
    ''' Ladder Bottom 梯底

    分组: Pattern Recognition 形态识别

    简介: 五日K线模式，下跌趋势中，前三日阴线， 开盘价与收盘价皆低于前一日开盘、收盘价，
    第四日倒锤头，第五日开盘价高于前一日开盘价， 阳线，收盘价高于前几日价格振幅，预示着底部反转。

    integer = CDLLADDERBOTTOM(open, high, low, close)
    '''
    return talib.CDLLADDERBOTTOM(open, high, low, close)


def CDLLONGLEGGEDDOJI(open, high, low, close):
    ''' Long Legged Doji 长脚十字

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，开盘价与收盘价相同居当日价格中部，上下影线长，
    表达市场不确定性。

    integer = CDLLONGLEGGEDDOJI(open, high, low, close)
    '''
    return talib.CDLLONGLEGGEDDOJI(open, high, low, close)


def CDLLONGLINE(open, high, low, close):
    ''' Long Line Candle 长蜡烛

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，K线实体长，无上下影线。

    integer = CDLLONGLINE(open, high, low, close)
    '''
    return talib.CDLLONGLINE(open, high, low, close)


def CDLMARUBOZU(open, high, low, close):
    ''' Marubozu 光头光脚/缺影线

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，上下两头都没有影线的实体，
    阴线预示着熊市持续或者牛市反转，阳线相反。

    integer = CDLMARUBOZU(open, high, low, close)
    '''
    return talib.CDLMARUBOZU(open, high, low, close)


def CDLMATCHINGLOW(open, high, low, close):
    ''' Matching Low 相同低价

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，下跌趋势中，第一日长阴线， 第二日阴线，
    收盘价与前一日相同，预示底部确认，该价格为支撑位。

    integer = CDLMATCHINGLOW(open, high, low, close)
    '''
    return talib.CDLMATCHINGLOW(open, high, low, close)


def CDLMATHOLD(open, high, low, close, penetration=0):
    ''' Mat Hold 铺垫

    分组: Pattern Recognition 形态识别

    简介: 五日K线模式，上涨趋势中，第一日阳线，第二日跳空高开影线，
    第三、四日短实体影线，第五日阳线，收盘价高于前四日，预示趋势持续。

    integer = CDLMATHOLD(open, high, low, close, penetration=0)
    '''
    return talib.CDLMATHOLD(open, high, low, close, penetration)


def CDLMORNINGDOJISTAR(open, high, low, close, penetration=0):
    ''' Morning Doji Star 十字晨星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式， 基本模式为晨星，第二日K线为十字星，预示底部反转。

    integer = CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
    '''
    return talib.CDLMORNINGDOJISTAR(open, high, low, close, penetration)


def CDLMORNINGSTAR(open, high, low, close, penetration=0):
    ''' Morning Star 晨星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，下跌趋势，第一日阴线， 第二日价格振幅较小，第三天阳线，预示底部反转。

    integer = CDLMORNINGSTAR(open, high, low, close, penetration=0)
    '''
    return talib.CDLMORNINGSTAR(open, high, low, close, penetration)


def CDLONNECK(open, high, low, close):
    ''' On-Neck Pattern 颈上线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，
    收盘价与前一日最低价相同，阳线，实体较短，预示着延续下跌趋势。

    integer = CDLONNECK(open, high, low, close)
    '''
    return talib.CDLONNECK(open, high, low, close)


def CDLPIERCING(open, high, low, close):
    ''' Piercing Pattern 刺透形态

    分组: Pattern Recognition 形态识别

    简介: 两日K线模式，下跌趋势中，第一日阴线，第二日收盘价低于前一日最低价，
    收盘价处在第一日实体上部，预示着底部反转。

    integer = CDLPIERCING(open, high, low, close)
    '''
    return talib.CDLPIERCING(open, high, low, close)


def CDLRICKSHAWMAN(open, high, low, close):
    ''' Rickshaw Man 黄包车夫

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，与长腿十字线类似， 若实体正好处于价格振幅中点，称为黄包车夫。

    integer = CDLRICKSHAWMAN(open, high, low, close)
    '''
    return talib.CDLRICKSHAWMAN(open, high, low, close)


def CDLRISEFALL3METHODS(open, high, low, close):
    ''' Rising/Falling Three Methods 上升/下降三法

    分组: Pattern Recognition 形态识别

    简介: 五日K线模式，以上升三法为例，上涨趋势中，
    第一日长阳线，中间三日价格在第一日范围内小幅震荡，
    第五日长阳线，收盘价高于第一日收盘价，预示股价上升。

    integer = CDLRISEFALL3METHODS(open, high, low, close)
    '''
    return talib.CDLRISEFALL3METHODS(open, high, low, close)


def CDLSEPARATINGLINES(open, high, low, close):
    ''' Separating Lines 分离线

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，上涨趋势中，第一日阴线，第二日阳线，
    第二日开盘价与第一日相同且为最低价，预示着趋势继续。

    integer = CDLSEPARATINGLINES(open, high, low, close)
    '''
    return talib.CDLSEPARATINGLINES(open, high, low, close)


def CDLSHOOTINGSTAR(open, high, low, close):
    ''' Shooting Star 射击之星

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，上影线至少为实体长度两倍，
    没有下影线，预示着股价下跌

    integer = CDLSHOOTINGSTAR(open, high, low, close)
    '''
    return talib.CDLSHOOTINGSTAR(open, high, low, close)


def CDLSHORTLINE(open, high, low, close):
    ''' Short Line Candle 短蜡烛

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，实体短，无上下影线

    integer = CDLSHORTLINE(open, high, low, close)
    '''
    return talib.CDLSHORTLINE(open, high, low, close)


def CDLSPINNINGTOP(open, high, low, close):
    ''' Spinning Top 纺锤

    分组: Pattern Recognition 形态识别

    简介: 一日K线，实体小。

    integer = CDLSPINNINGTOP(open, high, low, close)
    '''
    return talib.CDLSPINNINGTOP(open, high, low, close)


def CDLSTALLEDPATTERN(open, high, low, close):
    ''' Stalled Pattern 停顿形态

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，上涨趋势中，第二日长阳线，
    第三日开盘于前一日收盘价附近，短阳线，预示着上涨结束

    integer = CDLSTALLEDPATTERN(open, high, low, close)
    '''
    return talib.CDLSTALLEDPATTERN(open, high, low, close)


def CDLSTICKSANDWICH(open, high, low, close):
    ''' Stick Sandwich 条形三明治

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，第一日长阴线，第二日阳线，开盘价高于前一日收盘价，
    第三日开盘价高于前两日最高价，收盘价于第一日收盘价相同。

    integer = CDLSTICKSANDWICH(open, high, low, close)
    '''
    return talib.CDLSTICKSANDWICH(open, high, low, close)


def CDLTAKURI(open, high, low, close):
    ''' Takuri (Dragonfly Doji with very long lower shadow) 探水竿

    分组: Pattern Recognition 形态识别

    简介: 一日K线模式，大致与蜻蜓十字相同，下影线长度长。

    integer = CDLTAKURI(open, high, low, close)
    '''
    return talib.CDLTAKURI(open, high, low, close)


def CDLTASUKIGAP(open, high, low, close):
    ''' Tasuki Gap 跳空并列阴阳线

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，分上涨和下跌，以上升为例， 前两日阳线，第二日跳空，
    第三日阴线，收盘价于缺口中，上升趋势持续。

    integer = CDLTASUKIGAP(open, high, low, close)
    '''
    return talib.CDLTASUKIGAP(open, high, low, close)


def CDLTHRUSTING(open, high, low, close):
    ''' Thrusting Pattern 插入

    分组: Pattern Recognition 形态识别

    简介: 二日K线模式，与颈上线类似，下跌趋势中，第一日长阴线，第二日开盘价跳空，
    收盘价略低于前一日实体中部，与颈上线相比实体较长，预示着趋势持续。

    integer = CDLTHRUSTING(open, high, low, close)
    '''
    return talib.CDLTHRUSTING(open, high, low, close)


def CDLTRISTAR(open, high, low, close):
    ''' Tristar Pattern 三星

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，由三个十字组成， 第二日十字必须高于或者低于第一日和第三日，预示着反转。

    integer = CDLTRISTAR(open, high, low, close)
    '''
    return talib.CDLTRISTAR(open, high, low, close)


def CDLUNIQUE3RIVER(open, high, low, close):
    ''' Unique 3 River 奇特三河床

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，下跌趋势中，第一日长阴线，第二日为锤头，最低价创新低，第三日开盘价低于第二日收盘价，收阳线，
    收盘价不高于第二日收盘价，预示着反转，第二日下影线越长可能性越大。

    integer = CDLUNIQUE3RIVER(open, high, low, close)
    '''
    return talib.CDLUNIQUE3RIVER(open, high, low, close)


def CDLUPSIDEGAP2CROWS(open, high, low, close):
    ''' Upside Gap Two Crows 向上跳空的两只乌鸦

    分组: Pattern Recognition 形态识别

    简介: 三日K线模式，第一日阳线，第二日跳空以高于第一日最高价开盘，
    收阴线，第三日开盘价高于第二日，收阴线，与第一日比仍有缺口。

    integer = CDLUPSIDEGAP2CROWS(open, high, low, close)
    '''
    return talib.CDLUPSIDEGAP2CROWS(open, high, low, close)


def CDLXSIDEGAP3METHODS(open, high, low, close):
    ''' Upside/Downside Gap Three Methods 上升/下降跳空三法

    分组: Pattern Recognition 形态识别

    简介: 五日K线模式，以上升跳空三法为例，上涨趋势中，第一日长阳线，第二日短阳线，第三日跳空阳线，第四日阴线，
    开盘价与收盘价于前两日实体内， 第五日长阳线，收盘价高于第一日收盘价，预示股价上升。

    integer = CDLXSIDEGAP3METHODS(open, high, low, close)
    '''
    return talib.CDLXSIDEGAP3METHODS(open, high, low, close)
