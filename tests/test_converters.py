"""Basic tests for converters — leaves primes and stats uncovered."""

from numutils.converters import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0


def test_round_trip():
    assert abs(fahrenheit_to_celsius(celsius_to_fahrenheit(25)) - 25) < 1e-9
