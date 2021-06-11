from math_series import __version__

from math_series.series import fibonacci, fib_iterate, lucas


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_iterate_zero():
    actual = fib_iterate(0)
    expected = 0
    assert actual == expected


def fib_iterate_one():
    actual = fib_iterate(1)
    expected = 1
    assert actual == expected


def test_lucas_zero():
    actual = lucas(0)
    expected = 0
    assert actual != expected


def lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


# def test_one():
# 	actual = 'fizz_buzz'
# 	expected = '1'
# 	assert actual == expected
