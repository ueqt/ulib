# ulib
wrapper for TA-Lib, provide intellisense in vscode and PyCharm

support tdx like expression functions

让TA-Lib支持智能感知

提供类似通达信、同花顺、文华财经、麦语言等方式的函数

## Usage

```bash
pip install ulib
```

```python
import numpy
import ulib
close = numpy.random.random(100)
ulib.SMA(close)
```

or

```python
import numpy
from ulib import *
close = numpy.random.random(100)
SMA(close)
```

# Publish

```bash
python3 setup.py clean bdist_wheel upload
```

## Reference

[ta-lib](https://github.com/mrjbq7/ta-lib)
[talib-document](https://github.com/HuaRongSAO/talib-document)
[funcat](https://github.com/cedricporter/funcat)