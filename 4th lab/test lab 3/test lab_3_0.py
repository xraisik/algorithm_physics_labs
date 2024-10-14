import unittest
from typing import Callable

class TestReverseArray(unittest.TestCase):
    def setUp(self) -> None:
        self.func = self._buildTestedFunction()
    @staticmethod
    def _buildTestedFunction() -> Callable[[list[int]], list[int]]:
        from lab_3_0 import reverse_exercise
        return reverse_exercise

    def test_1_5_10_2(self):
        initial_array = [1, 5, 10, 2]

        reversed_array = [2, 10, 5, 1]

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)

    def test_7_3_8(self):
        initial_array = [7, 3, 8]

        reversed_array = [8, 3, 7]

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)

    def test_empty(self):
        initial_array = []

        reversed_array = []

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)

    def test_negative_numbers(self):
        initial_array = [-7, -8, -9]

        reversed_array = [-9, -8, -7]

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)

    def test_single_element(self):
        initial_array = [13]

        reversed_array = [13]

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)

    def test_strings_in_array(self):
        initial_array = ["c", "x", "z"]

        reversed_array = ["z", "x", "c"]

        actual_result = self.func(initial_array)

        self.assertEqual(reversed_array, actual_result)