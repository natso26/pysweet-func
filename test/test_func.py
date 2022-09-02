from pysweet import pack_, compose_


class TestFunc:
    def test_pack_(self):
        assert pack_(lambda x, y: x + y)(('a', 'b')) == 'ab'

    def test_compose_(self):
        assert compose_(
            lambda x: x + 'a',
            lambda x: x + 'b',
        )('c') == 'cab'
