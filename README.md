# pysweet-func

![test](https://github.com/natso26/pysweet-func/actions/workflows/test.yml/badge.svg?branch=main&event=push)
[![codecov](https://codecov.io/gh/natso26/pysweet-func/branch/main/graph/badge.svg)](https://codecov.io/gh/natso26/pysweet-func)
[![Documentation Status](https://readthedocs.org/projects/pysweet-func/badge/?version=latest)](https://pysweet-func.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pysweet-func.svg)](https://badge.fury.io/py/pysweet-func)

## Features

### Fluent iterable

```python
from pysweet import Iterable_

Iterable_([1, 2]).map(lambda x: x + 1).to_list()
# [2, 3]
```

### Multi-expression lambda

```python
from pysweet import block_

(lambda: block_(x := 1, x + 1))()
# 2
```

### Statements as expressions

```python
from pysweet import if_, try_, raise_

if_(True, lambda: 1, lambda: 2)
# 1

try_(lambda: raise_(Exception('test')), catch=lambda e: str(e))
# 'test'
```

## Resources

- [Read the Docs](https://pysweet-func.readthedocs.io)
- [PyPI](https://pypi.org/project/pysweet-func)
