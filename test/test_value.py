from pysweet import Value_


class TestValue:
    def test_val(self):
        assert Value_('a').val == 'a'

    def test_pipe(self):
        assert Value_('a').pipe(lambda x: x + 'b')._val == 'ab'
