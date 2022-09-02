from abc import abstractmethod
from typing import TypeVar, Coroutine, Any, Callable, ParamSpec, Generic

_P = ParamSpec('_P')
_S = TypeVar('_S')
_T = TypeVar('_T')

SimpleCoroutine = Coroutine[Any, Any, _T]

Callback = Callable[[], _T]

Transform = Callable[[_S], _T]

AsyncCallable = Callable[_P, SimpleCoroutine[_T]]

_Pipeable = TypeVar('_Pipeable', bound='Pipable')


class Pipeable_(Generic[_Pipeable, _S]):
    @property
    @abstractmethod
    def val(self) -> _S:
        pass

    @abstractmethod
    def pipe(self, f: Transform[_S, _T]) -> '_Pipeable[_T]':
        pass


_Chainable = TypeVar('_Chainable', bound='Chainable')


class Chainable_(Generic[_Chainable, _S]):
    @abstractmethod
    def flat_map(self, f: Transform[_S, '_Chainable[_T]']) -> '_Chainable[_T]':
        pass

    @abstractmethod
    def map(self, f: Transform[_S, _T]) -> '_Chainable[_T]':
        pass
