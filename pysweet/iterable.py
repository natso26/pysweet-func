from collections import deque
from itertools import chain
from typing import Iterable, TypeVar, Iterator, List, Union, Any

from pysweet.types import Transform, Pipeable_, Chainable_

_A = TypeVar('_A')
_B = TypeVar('_B')


# noinspection PyPep8Naming
class Iterable_(Iterable[_A], Pipeable_['Iterable_', Iterable[_A]], Chainable_['Iterable_', _A]):
    """
    ``Iterable`` with method chaining.

    Args:
        it: Wrapped ``Iterable``.
    """

    _it: Iterable[_A]

    def __init__(self, it: Iterable[_A]):
        self._it = it

    def __iter__(self) -> Iterator[_A]:
        return self._it.__iter__()

    @property
    def val(self) -> Iterable[_A]:
        """
        Get underlying ``Iterable``.

        >>> Iterable_([0, 1, 2]).val
        [0, 1, 2]

        Returns:
            Wrapped ``Iterable``.
        """

        return self._it

    def pipe(self, f: Transform[Iterable[_A], Iterable[_B]]) -> 'Iterable_[_B]':
        """
        Transform self with ``f`` immutably.

        >>> Iterable_([0, 1, 2]).pipe(lambda x: x + x).val
        [0, 1, 2, 0, 1, 2]

        Args:
            f: Function.

        Returns:
            Transformed ``Iterable_``.
        """

        return Iterable_(f(self._it))

    def map(self, f: Transform[_A, _B]) -> 'Iterable_[_B]':
        """
        Map ``f`` over self immutably.

        >>> Iterable_(range(5)).map(lambda x: x * 2).to_list()
        [0, 2, 4, 6, 8]

        Args:
            f: Function.

        Returns:
            Mapped ``Iterable_``.
        """

        return Iterable_(map(f, self._it))

    def filter(self, f: Transform[_A, Any]) -> 'Iterable_[_A]':
        """
        Filter ``f`` over self immutably.

        >>> Iterable_(range(5)).filter(lambda x: x % 2 == 0).to_list()
        [0, 2, 4]

        Args:
            f: Function.

        Returns:
            Filtered ``Iterable_``.
        """

        return Iterable_(filter(f, self._it))

    def flat_map(self, f: Transform[_A, Iterable[_B]]) -> 'Iterable_[_B]':
        """
        Map ``f`` over self and chain results, immutably.

        >>> Iterable_(range(5)).flat_map(lambda x: [x, x + 1]).to_list()
        [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

        Args:
            f: Function.

        Returns:
            Flat-mapped ``Iterable_``.
        """

        return Iterable_(chain.from_iterable(map(f, self._it)))

    def extend(self, it: Iterable[_B]) -> 'Iterable_[Union[_A, _B]]':
        """
        Chain self with another ``Iterable``, immutably.

        >>> Iterable_(range(5)).extend([5, 6]).to_list()
        [0, 1, 2, 3, 4, 5, 6]

        Args:
            it: ``Iterable``.

        Returns:
            Extended ``Iterable_``.
        """

        return Iterable_(chain(self._it, it))

    def zip(self) -> 'Iterable_[tuple]':
        """
        Zip self immutably.

        >>> Iterable_(dict(a=1, b=2).items()).zip().to_list()
        [('a', 'b'), (1, 2)]

        Returns:
            Zipped ``Iterable_``.
        """

        return Iterable_(zip(*self._it))

    def consume(self) -> None:
        """
        Iterate over self.

        >>> Iterable_(range(3)).map(print).consume()
        0
        1
        2

        Returns:
            None.
        """

        deque(self._it, maxlen=0)

    def to_list(self) -> List[_A]:
        """
        Unwrap underlying ``Iterable`` as a ``list``.

        >>> Iterable_(range(5)).to_list()
        [0, 1, 2, 3, 4]

        Returns:
            Wrapped ``Iterable`` converted to ``list``.
        """

        return list(self._it)

    def to_dict(self) -> dict:
        """
        Unwrap underlying ``Iterable`` as a ``dict``.

        >>> Iterable_([('a', 1), ('b', 2)]).to_dict()
        {'a': 1, 'b': 2}

        Returns:
            Wrapped ``Iterable`` converted to ``dict``.
        """

        return dict(self._it)
