import itertools
from typing import Iterable, TypeVar, Callable, Iterator, Any, List

A = TypeVar('A')
B = TypeVar('B')


class Iterable_(Iterable[A]):
    _it: Iterable[A]

    def __init__(self, it: Iterable[A]):
        self._it = it

    def __iter__(self) -> Iterator[A]:
        return iter(self._it)

    def map(self, f: Callable[[A], B]) -> 'Iterable_[B]':
        return Iterable_(map(f, self._it))

    def filter(self, f: Callable[[A], Any]) -> 'Iterable_[A]':
        return Iterable_(filter(f, self._it))

    def flat_map(self, f: Callable[[A], Iterable[B]]) -> 'Iterable_[B]':
        return Iterable_(itertools.chain.from_iterable(map(f, self._it)))

    def extend(self, it: Iterable[A]) -> 'Iterable_[A]':
        return Iterable_(itertools.chain(self._it, it))

    def zip(self) -> 'Iterable_':
        return Iterable_(zip(*self._it))

    def to_list(self) -> List[A]:
        return list(self._it)

    def to_dict(self) -> dict:
        return dict(self._it)
