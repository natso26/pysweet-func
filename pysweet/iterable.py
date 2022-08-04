import itertools
from typing import Iterable, TypeVar, Callable, Iterator, Any, List

A = TypeVar('A')
B = TypeVar('B')


class Iterable_(Iterable[A]):
    """
    An ``Iterable`` wrapping ``it`` with the same ``Iterator`` as ``it``.

    Args:
        it: ``Iterable``.
    """
    _it: Iterable[A]

    def __init__(self, it: Iterable[A]):
        self._it = it

    def __iter__(self) -> Iterator[A]:
        return self._it.__iter__()

    def map(self, f: Callable[[A], B]) -> 'Iterable_[B]':
        """
        Map ``f`` over the wrapped ``Iterable``,
        and rewrap as a new ``Iterable_``.

        >>> Iterable_(range(5)).map(lambda x: x * 2).to_list()
        [0, 2, 4, 6, 8]

        Args:
            f: Function.

        Returns:
            Mapped ``Iterable_``.
        """
        return Iterable_(map(f, self._it))

    def filter(self, f: Callable[[A], Any]) -> 'Iterable_[A]':
        """
        Filter ``f`` over the wrapped ``Iterable``,
        and rewrap as a new ``Iterable_``.

        >>> Iterable_(range(5)).filter(lambda x: x % 2 == 0).to_list()
        [0, 2, 4]

        Args:
            f: Function.

        Returns:
            Filtered ``Iterable_``.
        """
        return Iterable_(filter(f, self._it))

    def flat_map(self, f: Callable[[A], Iterable[B]]) -> 'Iterable_[B]':
        """
        Chain the results of mapping ``f`` over the wrapped ``Iterable``,
        and rewrap as a new ``Iterable_``.

        >>> Iterable_(range(5)).flat_map(lambda x: [x, x + 1]).to_list()
        [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

        Args:
            f: Function.

        Returns:
            Flat-mapped ``Iterable_``.
        """
        return Iterable_(itertools.chain.from_iterable(map(f, self._it)))

    def extend(self, it: Iterable[A]) -> 'Iterable_[A]':
        """
        Chain the wrapped ``Iterable`` with ``it``,
        and rewrap as a new ``Iterable_``.

        >>> Iterable_(range(5)).extend([5, 6]).to_list()
        [0, 1, 2, 3, 4, 5, 6]

        Args:
            it: ``Iterable``.

        Returns:
            Extended ``Iterable_``.
        """
        return Iterable_(itertools.chain(self._it, it))

    def zip(self) -> 'Iterable_':
        """
        Zip the wrapped ``Iterable``,
        and rewrap as a new ``Iterable_``.

        >>> Iterable_(dict(a=1, b=2).items()).zip().to_list()
        [('a', 'b'), (1, 2)]

        Returns:
            Zipped ``Iterable_``.
        """
        return Iterable_(zip(*self._it))

    def to_list(self) -> List[A]:
        """
        Return the wrapped ``Iterable``
        converted to ``list``.

        >>> Iterable_(range(5)).to_list()
        [0, 1, 2, 3, 4]

        Returns:
            Wrapped ``Iterable`` converted to ``list``.
        """
        return list(self._it)

    def to_dict(self) -> dict:
        """
        Return the wrapped ``Iterable``
        converted to ``dict``.

        >>> Iterable_([('a', 1), ('b', 2)]).to_dict()
        {'a': 1, 'b': 2}

        Returns:
            Wrapped ``Iterable`` converted to ``dict``.
        """
        return dict(self._it)
