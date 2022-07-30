from pysweet import Iterable_


class TestIterable:
    def test_iter(self):
        assert list(
            Iterable_(['a', 'b', 'c'])
        ) == ['a', 'b', 'c']

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

    def test_to_list(self):
        assert Iterable_(['a', 'b', 'c']).to_list() == ['a', 'b', 'c']

    def test_to_dict(self):
        assert Iterable_([('a', 1), ('b', 2), ('c', 3)]).to_dict() == {'a': 1, 'b': 2, 'c': 3}
