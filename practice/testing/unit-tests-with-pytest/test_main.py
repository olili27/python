from main import add


def test_add_with_positive_integers():
    assert add(1, 2) == 3
    assert add(2, 2) == 4


def test_add_with_negative_integers():
    assert add(-1, -2) == -3
    assert add(-2, -2) == -4


def test_add_with_positive_n_negative_integers():
    assert add(-1, 2) == 1
    assert add(-2, 2) == 0


if __name__ == "__main__":
    pass
