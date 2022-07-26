from typing import TypeVar, Coroutine, Any, Callable

__all__ = [
    'SimpleCoroutine',
    'Lazy',
    'AsyncLazy',
    'Transform',
    'AsyncTransform',
]

_S = TypeVar('_S')
_T = TypeVar('_T')

SimpleCoroutine = Coroutine[Any, Any, _T]

Lazy = Callable[[], _T]

AsyncLazy = Callable[[], SimpleCoroutine[_T]]

Transform = Callable[[_S], _T]

AsyncTransform = Transform[_S, SimpleCoroutine[_T]]
