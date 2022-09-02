from abc import abstractmethod
from typing import TypeVar, Coroutine, Any, Callable, Generic

_S = TypeVar('_S')
_T = TypeVar('_T')

SimpleCoroutine = Coroutine[Any, Any, _T]

Lazy = Callable[[], _T]

Transform = Callable[[_S], _T]

AsyncTransform = Transform[_S, SimpleCoroutine]

_Pipeable = TypeVar('_Pipeable', bound='Pipeable_')


# noinspection PyPep8Naming
class Pipeable_(Generic[_Pipeable, _S]):
    @property
    @abstractmethod
    def val(self) -> _S:
        pass

    @abstractmethod
    def pipe(self, f: Transform[_S, _T]) -> '_Pipeable[_T]':
        pass


_Chainable = TypeVar('_Chainable', bound='Chainable_')


# noinspection PyPep8Naming
class Chainable_(Generic[_Chainable, _S]):
    @abstractmethod
    def flat_map(self, f: Transform[_S, '_Chainable[_T]']) -> '_Chainable[_T]':
        pass

    @abstractmethod
    def map(self, f: Transform[_S, _T]) -> '_Chainable[_T]':
        pass
