# py-sweetfunc

Light syntactic sugar for composable Python programs

## Features

### Fluent iterable

```python
from py_sweetfunc import Iterable_

val = (
    Iterable_([1, 2])
    .map(lambda x: x + 1)
    .to_list()
)
# val == [2, 3]
```

### Multiline lambda

```python
from py_sweetfunc import block_

val = lambda: block_(
    x := 1,
    x + 1,
)
# val() == 2
```

### Statements as expressions

```python
from py_sweetfunc import try_, raise_

val = try_(
    lambda: 1 / 0,
    catch=lambda e: raise_(ValueError())
)
# raises ValueError()
```
