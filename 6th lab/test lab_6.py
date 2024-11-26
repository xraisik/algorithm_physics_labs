import pytest
import time
from lab_6 import fibonacci, fibonacci_nc

def test_fibonacci_values():
    expected_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

    for i, expected in enumerate(expected_values):
        assert fibonacci(i) == expected, f"Error at index {i}: {fibonacci(i)} != {expected}"
        assert fibonacci_nc(i) == expected, f"Error at index {i}: {fibonacci_nc(i)} != {expected}"

def test_fibonacci_performance():
    n = 30
    repetitions = 5

    # not cached
    start_time = time.time()
    for _ in range(repetitions):
        fibonacci_nc(n)
    nc_time = (time.time() - start_time) / repetitions

    # cached
    start_time = time.time()
    for _ in range(repetitions):
        fibonacci(n)
    cached_time = (time.time() - start_time) / repetitions

    print(f"Average time for fibonacci_nc({n}): {nc_time:.6f} seconds")
    print(f"Average time for fibonacci({n}): {cached_time:.6f} seconds")
