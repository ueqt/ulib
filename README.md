# talib
wrapper for TA-Lib, provide intellisense in vscode and PyCharm

让TA-Lib支持智能感知

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

# Publish

```bash
python3 setup.py bdist_wheel upload
```

## Reference

[ta-lib](https://github.com/mrjbq7/ta-lib)
[talib-document](https://github.com/HuaRongSAO/talib-document)