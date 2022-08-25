from typing import ContextManager

import pytest

from pysweet import block_, if_, raise_, try_, with_


class TestBlock:
    def test_block(self):
        assert block_(
            x := 'a',
            x + 'b',
        ) == 'ab'

    def test_if(self):
        assert if_('b' > 'a', lambda: 'c', lambda: 'd') == 'c'
        assert if_('b' < 'a', lambda: 'c', lambda: 'd') == 'd'

        assert if_(1, lambda: 'c', lambda: 'd') == 'c'
        assert if_(0, lambda: 'c', lambda: 'd') == 'd'

    def test_try(self):
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

    def test_raise(self):
        class MyException(Exception):
            pass

        with pytest.raises(MyException):
            raise_(MyException())

    def test_with(self):
        exited = False

        class MyContextManager(ContextManager):
            def __enter__(self):
                return 'a'

            def __exit__(self, exc_type, exc_value, traceback):
                nonlocal exited
                exited = True

        assert with_(MyContextManager(), lambda x: x + 'b') == 'ab'
        assert exited
