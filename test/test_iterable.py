from pysweet import Iterable_


class TestIterable:
    def test___iter__(self):
        assert list(
            Iterable_(['a', 'b', 'c'])
        ) == ['a', 'b', 'c']

    def test_val(self):
        assert Iterable_(['a', 'b', 'c']).val == ['a', 'b', 'c']

    def test_pipe(self):
        assert Iterable_(['a', 'b', 'c']).pipe(lambda x: x + ['d'])._it == ['a', 'b', 'c', 'd']

    def test_map(self):
        assert list(
            Iterable_(['a', 'b', 'c']).map(lambda x: x + 'z')._it
        ) == ['az', 'bz', 'cz']

    def test_filter(self):
        assert list(
            Iterable_(['a', 'b', 'c']).filter(lambda x: x != 'b')._it
        ) == ['a', 'c']

    def test_flat_map(self):
        assert list(
            Iterable_(['a', 'b', 'c']).flat_map(lambda x: [x + 'z', x + 'w'])._it
        ) == ['az', 'aw', 'bz', 'bw', 'cz', 'cw']

    def test_extend(self):
        assert list(
            Iterable_(['a', 'b', 'c']).extend(['d', 'e'])._it
        ) == ['a', 'b', 'c', 'd', 'e']

    def test_zip(self):
        assert list(
            Iterable_([['a', 'b'], ['c', 'd'], ['e', 'f']]).zip()._it
        ) == [('a', 'c', 'e'), ('b', 'd', 'f')]

    def test_consume(self):
        acc = []

        iterable = Iterable_((acc.append(x) for x in ['a', 'b', 'c']))
        assert acc == []

        iterable.consume()
        assert acc == ['a', 'b', 'c']

    def test_to_list(self):
        assert Iterable_(['a', 'b', 'c']).to_list() == ['a', 'b', 'c']

    def test_to_dict(self):
        assert Iterable_([('a', 1), ('b', 2), ('c', 3)]).to_dict() == {'a': 1, 'b': 2, 'c': 3}
