from typing import Any, Callable, TypeVar, NoReturn

T = TypeVar('T')


def block_(*args):
    return args[-1]


def if_(condition: Any, then_do: Callable[[], T], else_do: Callable[[], T]) -> T:
    if condition:
        return then_do()
    else:
        return else_do()


def raise_(exception: Exception) -> NoReturn:
    raise exception


def try_(do: Callable[[], T], catch: Callable[[Exception], T]) -> T:
    try:
        return do()
    except Exception as e:
        return catch(e)
