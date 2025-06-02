import pytest

def add_numbers(a, b):
	return a + b

def test_zip():
    a_values = [1, 2, 3, 4]
    b_values = [10, 20, 30, 4]
    expected = [11, 22, 33, 8]
    for (a, b), exp in zip(zip(a_values, b_values), expected):
        assert add_numbers(a, b) == exp, f"Помилка: {a} + {b} != {exp}"
