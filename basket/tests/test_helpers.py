from basket.helpers import pairs


def test_pairs():
    a = [1, 2, 3, 4, 5]
    assert list(pairs(a)) == [(1, 2), (2, 3), (3, 4), (4, 5)]
