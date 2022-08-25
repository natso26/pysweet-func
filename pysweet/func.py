from typing import Callable, TypeVar, Any

_T = TypeVar('_T')


def pack_(func: Callable[..., _T]) -> Callable[[tuple], _T]:
    """
    Return a single-argument function that sends
    ``(x, y, ...)`` to ``func(x, y, ...)``.

    >>> list(map(pack_(lambda x, y: x + y), [(1, 2), (3, 4)]))
    [3, 7]

    Args:
        func: Function.

    Returns:
        Function with a single packed argument.
    """

    def packed(args: tuple) -> _T:
        return func(*args)

    return packed


def compose_(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Compose elements of ``funcs``, sending
    ``x`` to ``funcs[-1](funcs[-2](...(funcs[0](x))...))``.

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
