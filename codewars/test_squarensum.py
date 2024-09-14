# Complete the square sum function so that it squares each number passed into it and then sums the results together.


def square_sum(numbers: list[int]) -> int:
    new_variable = 0
    for num in numbers:
        print(f"new var esta valiendo {new_variable} ")
        print(f"el dato pelado es {num}")
        print(f"el dato al cuadrado es {num**2}")

        new_variable = new_variable + num**2
        print(f"ahora vale {new_variable=}")
    return new_variable


square_sum(numbers=[1, 2])


def test_basic_test_cases():
    assert square_sum([1, 2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50
    assert square_sum([]) == 0
    assert square_sum([-1, -2]) == 5
    assert square_sum([-1, 0, 1]) == 2
