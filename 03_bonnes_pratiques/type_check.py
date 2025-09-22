import math
from typing import overload, Literal, Generic, TypeVar

T = TypeVar("T", bound=int | float)


def bad_type(x: float) -> str:
    # Should be fairly easy to fix
    print(f"x = {x}")


class Point(Generic[T]):
    def __init__(self, x: T, y: T):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Point | float") -> "Point[T]":
        if isinstance(other, "Point"):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    def __eq__(self, value) -> bool:
        if not isinstance(value, Point):
            return False
        return self.x == value.x and self.y == value.y

    def __abs__(self) -> T:
        return max(abs(self.x), abs(self.y))

    def norm(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @overload
    def normalize(self, inplace: Literal[True]) -> None: ...
    @overload
    def normalize(self, inplace: Literal[False]) -> "Point[float]": ...
    def normalize(self, inplace: bool = False) -> "Point[float] | None":
        norm = self.norm()
        if inplace:
            self.x /= norm
            self.y /= norm
        else:
            return Point(self.x / norm, self.y / norm)


def point_form_sequence(input_list: list[T]) -> "Point[T]":
    return Point(input_list[0], input_list[1])


if __name__ == "__main__":
    my_point = Point(0, 1)
    value: int = abs(my_point)
    print(f"First point : {my_point}")
    print(f"Norm of this point : {value}")
    my_other_point = Point(0.5, 1)
    other_value: int = abs(my_other_point)
    print(f"First point : {my_point}")
    print(f"Norm of this point : {other_value}")
    my_last_point = point_form_sequence(input_list=(0, 1))
    print(f"Thrid point: {my_last_point}")
