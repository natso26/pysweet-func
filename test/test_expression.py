from asyncio import sleep, run, iscoroutine
from typing import ContextManager, AsyncContextManager

import pytest

from pysweet import block_, if_, raise_, try_, with_, async_block_, await_, async_with_, async_try_


class TestExpression:
    def test_block_(self):
        assert block_(
            x := 'a',
            x + 'b',
        ) == 'ab'

    def test_if(self):
        assert if_('b' > 'a', lambda: 'c', lambda: 'd') == 'c'
        assert if_('b' < 'a', lambda: 'c', lambda: 'd') == 'd'

        assert if_(1, lambda: 'c', lambda: 'd') == 'c'
        assert if_(0, lambda: 'c', lambda: 'd') == 'd'

    def test_try_(self):
        def _raise(x):
            raise x

        assert try_(
            lambda: 'a',
            catch=lambda e: 'b',
        ) == 'a'

        assert try_(
            lambda: _raise(Exception('a')),
            catch=lambda e: str(e) + 'b',
        ) == 'ab'

    def test_raise_(self):
        class MyException(Exception):
            pass

        with pytest.raises(MyException):
            raise_(MyException())

    def test_with_(self):
        exited = False

        class MyContextManager(ContextManager):
            def __enter__(self):
                return 'a'

            def __exit__(self, exc_type, exc_value, traceback):
                nonlocal exited
                exited = True

        assert with_(MyContextManager(), lambda x: x + 'b') == 'ab'
        assert exited

    def test_async_block__await_(self):
        async def coro(x):
            await sleep(0.0001)

            nonlocal count
            count += 1

            return x + 'b'

        count = 0

        result = run(async_block_(
            lambda _: coro('a'),
        ))

        assert iscoroutine(result)
        assert count == 0

        assert run(result) == 'ab'
        assert count == 1

        count = 0

        result = run(async_block_(
            await_(lambda _: coro('a')),
        ))

        assert result == 'ab'
        assert count == 1

        count = 0

        result = run(async_block_(
            await_(lambda _: coro('a')),
            lambda x: x + 'c',
        ))

        assert result == 'abc'
        assert count == 1

        count = 0

        result = run(async_block_(
            lambda _: 'a',
            await_(coro),
            lambda x: x + 'c',
        ))

        assert result == 'abc'
        assert count == 1

        count = 0

        result = run(async_block_(
            lambda _: 'a',
            await_(coro),
            lambda x: x + 'c',
            await_(coro),
        ))

        assert result == 'abcb'
        assert count == 2

    def test_async_try_(self):
        async def do_ok():
            return 'a'

        async def do_err():
            raise Exception('b')

        async def catch(e):
            return str(e) + 'c'

        assert run(async_try_(do_ok, catch)) == 'a'

        assert run(async_try_(do_err, catch)) == 'bc'

    def test_async_with_(self):
        exited = False

        class MyAsyncContextManager(AsyncContextManager):
            async def __aenter__(self):
                return 'a'

            async def __aexit__(self, exc_type, exc_value, traceback) -> None:
                nonlocal exited
                exited = True

        async def do(x):
            return x + 'b'

        assert run(async_with_(MyAsyncContextManager(), do)) == 'ab'
        assert exited
