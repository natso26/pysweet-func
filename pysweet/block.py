from typing import Callable, TypeVar, NoReturn, Union, ContextManager, Any

_T = TypeVar('_T')
_S = TypeVar('_S')


def block_(*args: Any) -> Any:
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


def if_(condition: Any, then_do: Callable[[], _T], else_do: Callable[[], _S]) -> Union[_T, _S]:
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


def try_(do: Callable[[], _T], catch: Callable[[Exception], _S]) -> Union[_T, _S]:
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


def with_(context: ContextManager[_S], do: Callable[[_S], _T]) -> _T:
    """
    Execute ``do`` in the context of ``context``.

    >>> from threading import Lock
    >>> lock = Lock()
    >>> with_(lock, lambda _: 1)
    1

    Args:
        context: Context manager.
        do: Callback.

    Returns:
        Result of ``do``.
    """

    with context as ctx:
        return do(ctx)
