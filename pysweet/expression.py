from typing import TypeVar, NoReturn, Union, ContextManager, Any, Generic, AsyncContextManager

from pysweet.types import Transform, SimpleCoroutine, Lazy, AsyncTransform

__all__ = [
    'block_',
    'if_',
    'try_',
    'raise_',
    'with_',
    'async_block_',
    'await_',
    'async_with_',
]

_S = TypeVar('_S')
_T = TypeVar('_T')


def block_(*expressions: Any) -> Any:
    """
    Code block evaluating to the last expression.

    >>> val = lambda: block_(
    ...     x := 1,
    ...     x + 1,
    ... )
    >>> val()
    2

    Args:
        *expressions: Expressions.

    Returns:
        Last element of ``expressions``.
    """

    return expressions[-1]


def if_(condition: Any, then_do: Lazy[_S], else_do: Lazy[_T]) -> Union[_S, _T]:
    """
    ``if`` expression.

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


# noinspection PyShadowingNames
def try_(do: Lazy[_S], catch: Transform[Exception, _T]) -> Union[_S, _T]:
    """
    ``try`` expression.

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
    ``raise`` expression.

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


def with_(context: ContextManager[_S], do: Transform[_S, _T]) -> _T:
    """
    ``with`` expression.

    >>> from threading import Lock
    >>> lock = Lock()
    >>> with_(lock, lambda _: 1)
    1

    Args:
        context: Context manager.
        do: Callback.

    Returns:
        Result of ``do`` in the context of ``context``.
    """

    with context as ctx:
        return do(ctx)


def async_block_(*expressions: Union[Transform[Any, Any], '_Await[Any, Any]']) -> SimpleCoroutine[Any]:
    """
    Asynchronous code block evaluating expressions in order.
    Use ``await_`` to await a specific expression.

    >>> from asyncio import sleep, run
    ...
    >>> async def add_one(x):
    ...     await sleep(0.1)
    ...     return x + 1
    ...
    >>> main = lambda x: async_block_(
    ...     await_(lambda _: add_one(x)),
    ...     lambda y: y * 2,
    ...     await_(add_one),
    ...     print,
    ... )
    ...
    >>> run(main(1))
    5

    Args:
        *expressions: Expressions.

    Returns:
        Coroutine.
    """

    async def coro() -> Any:
        val: Any = None

        for expression in expressions:
            if isinstance(expression, _Await):
                # noinspection PyProtectedMember
                val = await expression._func(val)

            else:
                val = expression(val)

        return val

    return coro()


def await_(func: AsyncTransform[_S, _T]) -> '_Await[_S, _T]':
    """
    ``await`` expression.
    Only valid inside an ``async_block_``.

    Args:
        func: Asynchronous transform.

    Returns:
        Internal ``_Await`` object.
    """

    return _Await(func)


def async_with_(context: AsyncContextManager[_S], do: AsyncTransform[_S, _T]) -> SimpleCoroutine[_T]:
    """
    ``async with`` expression.

    >>> from asyncio import Lock, run
    >>> lock = Lock()
    >>> async def main():
    ...     return 1
    >>> run(async_with_(lock, lambda _: main()))
    1

    Args:
        context: Asynchronous context manager.
        do: Asynchronous callback.

    Returns:
        Coroutine running ``do`` in the context of ``context``.
    """

    async def coro() -> _T:
        async with context as ctx:
            return await do(ctx)

    return coro()


class _Await(Generic[_S, _T]):
    _func: AsyncTransform[_S, _T]

    def __init__(self, func: AsyncTransform[_S, _T]):
        self._func = func
