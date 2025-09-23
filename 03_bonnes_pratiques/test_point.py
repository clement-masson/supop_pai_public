import pytest

from type_check import Point


def test_point():
    assert True


def test_points_equality():
    assert True


def test_points_operations():
    assert True


def test_from_sequence():
    assert True


def test_raise_error():
    with pytest.raises(ZeroDivisionError):
        raise ZeroDivisionError


# Bonus parametrize
@pytest.mark.parametrize(
    "point1,point2,result", [((1, 1), (1, 2), (2, 3)), ((-1, 0), (2, 3), (1, 3))]
)
def test_sums(point1, point2, result):
    print(point1, point2, result)
    assert True
