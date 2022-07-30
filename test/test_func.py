from pysweet import pack_, compose_


class TestFunc:
    def test_pack(self):
        assert pack_(lambda x, y: x + y)(('a', 'b')) == 'ab'

    def test_compose(self):
        assert compose_(
            lambda x: x + 'a',
            lambda x: x + 'b',
        )('c') == 'cab'
