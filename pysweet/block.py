from typing import Any, Callable, TypeVar, NoReturn

T = TypeVar('T')


def block_(*args):
    """
    Return the last element of ``args``.
    Allow writing multi-expression lambdas.

    >>> val = lambda: block_(
    ...     x := 1,
    ...     x + 1,
    ... )
    >>> val()
    2

    Args:
        *args: Expressions.

    Returns:
        Last element of ``args``.
    """
    return args[-1]


def if_(condition: Any, then_do: Callable[[], T], else_do: Callable[[], T]) -> T:
    """
    Ternary operator in the natural order.
    If ``condition``, then do ``then_do``, else do ``else_do``.

    >>> if_(True, lambda: 1, lambda: 2)
    1

    Args:
        condition: Condition.
        then_do: Callback if ``condition`` is truthy.
        else_do: Callback if ``condition`` is falsy.

    Returns:
        Result of ``then_do`` or ``else_do``.
    """
    if condition:
        return then_do()
    else:
        return else_do()


def raise_(exception: Exception) -> NoReturn:
    """
    Raise ``exception``.
    Allow raising exceptions inside lambdas.

    >>> val = lambda: raise_(Exception('test'))
    >>> val()
    Traceback (most recent call last):
        ...
    Exception: test

    Args:
        exception: Exception.

    Returns:
        No return.
    """
    raise exception


def try_(do: Callable[[], T], catch: Callable[[Exception], T]) -> T:
    """
    Allow try-catch blocks inside lambdas.
    Try ``do``; catch exception with ``catch``.

    >>> val = lambda: try_(
    ...     lambda: 1,
    ...     catch=lambda e: 2,
    ... )
    >>> val()
    1

    Args:
        do: Callback.
        catch: Callback if ``do`` raises an exception.

    Returns:
        Result of ``do`` or ``catch``.
    """
    try:
        return do()
    except Exception as e:
        return catch(e)
