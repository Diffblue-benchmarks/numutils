"""Descriptive statistics utilities."""

from collections import Counter


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median of a list of numbers."""
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return float(sorted_vals[mid])


def mode(values: list[float]) -> float:
    """Return the most frequently occurring value. Raises ValueError if list is empty."""
    if not values:
        raise ValueError("Cannot compute mode of empty list")
    counts = Counter(values)
    return counts.most_common(1)[0][0]


def std_dev(values: list[float]) -> float:
    """Return the population standard deviation."""
    if not values:
        raise ValueError("Cannot compute std_dev of empty list")
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return variance**0.5
