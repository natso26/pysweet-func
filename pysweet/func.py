from typing import Callable, TypeVar

T = TypeVar('T')
S = TypeVar('S')


def pack_(func: Callable[..., T]) -> Callable[[S], T]:
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

    def packed(args):
        return func(*args)

    return packed


def compose_(*funcs: Callable) -> Callable[[S], T]:
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

    def composed(arg):
        for func in funcs:
            arg = func(arg)
        return arg

    return composed
