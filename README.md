# pysweet-func

![test](https://github.com/natso26/pysweet-func/actions/workflows/test.yml/badge.svg?branch=main&event=push)
[![codecov](https://codecov.io/gh/natso26/pysweet-func/branch/main/graph/badge.svg)](https://codecov.io/gh/natso26/pysweet-func)
[![PyPI version](https://badge.fury.io/py/pysweet-func.svg)](https://badge.fury.io/py/pysweet-func)

Light syntactic sugar for composable Python programs

## Features

### Fluent iterable

```python
from pysweet import Iterable_

val = (
    Iterable_([1, 2])
    .map(lambda x: x + 1)
    .to_list()
)
# val == [2, 3]
```

### Multiline lambda

```python
from pysweet import block_

val = lambda: block_(
    x := 1,
    x + 1,
)
# val() == 2
```

### Statements as expressions

```python
from pysweet import try_, raise_

val = try_(
    lambda: 1 / 0,
    catch=lambda e: raise_(ValueError())
)
# raises ValueError()
```
