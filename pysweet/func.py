from typing import Callable, TypeVar, Any

from pysweet.types import Transform

_T = TypeVar('_T')


def pack_(func: Callable[..., _T]) -> Transform[tuple, _T]:
    """
    Pack function arguments into a single ``tuple``.

    >>> list(map(pack_(lambda x, y: x + y), [(1, 2), (3, 4)]))
    [3, 7]

    Args:
        func: Function.

    Returns:
        Function mapping ``(x, y, ...)`` to ``func(x, y, ...)``.
    """

    def packed(args: tuple) -> _T:
        return func(*args)

    return packed


def compose_(*funcs: Transform[Any, Any]) -> Transform[Any, Any]:
    """
    Compose single-argument functions,
    evaluting from left to right.

    >>> compose_(lambda x: x + 1, lambda x: x * 2)(1)
    4

    Args:
        funcs: Functions.

    Returns:
        Composed function.
    """

    def composed(arg: Any) -> Any:
        for func in funcs:
            arg = func(arg)

        return arg

    return composed
