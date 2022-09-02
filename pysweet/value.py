from typing import TypeVar

from pysweet.types import Transform, Pipeable_

_A = TypeVar('_A')
_B = TypeVar('_B')


# noinspection PyPep8Naming
class Value_(Pipeable_['Value_', _A]):
    """
    Pipeable value.

    Args:
        val: Wrapped value.
    """

    _val: _A

    def __init__(self, val: _A):
        self._val = val

    @property
    def val(self) -> _A:
        """
        Get underlying value.

        >>> Value_(2).val
        2

        Returns:
            Wrapped value.
        """

        return self._val

    def pipe(self, f: Transform[_A, _B]) -> 'Value_[_B]':
        """
        Transform self with ``f`` immutably.

        >>> Value_(2).pipe(lambda x: x + 1).val
        3

        Args:
            f: Function.

        Returns:
            Transformed ``Value_``.
        """

        return Value_(f(self.val))
