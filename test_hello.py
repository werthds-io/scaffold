from hello import add


def test_add():
    """test adding 1 plus 2 and expect 3"""
    assert add(1, 2) == 3
