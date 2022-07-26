from pysweet import starred_, compose_


class TestFunc:
    def test_starred(self):
        assert starred_(lambda x, y: x + y)(('a', 'b')) == 'ab'

    def test_compose(self):
        assert compose_(
            lambda x: x + 'a',
            lambda x: x + 'b',
        )('c') == 'cab'
