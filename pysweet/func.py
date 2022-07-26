from typing import Callable, TypeVar

T = TypeVar('T')
S = TypeVar('S')


def starred_(func: Callable[..., T]) -> Callable[[S], T]:
    def starred(v):
        return func(*v)

    return starred


def compose_(*funcs: Callable) -> Callable[[S], T]:
    def composed(v):
        for func in funcs:
            v = func(v)
        return v

    return composed
