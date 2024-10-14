import unittest
from typing import Callable

class TestGetNumberInBetween(unittest.TestCase):
    def setUp(self) -> None:
        self.func = self._buildTestedFunction()
    @staticmethod
    def _buildTestedFunction() -> Callable[[list[int], list[int]], list[int]]:
        from lab_3_1 import get_numbers_in_between
        return get_numbers_in_between

    def test_2_4_32_16_96(self):
        a = [2, 4]
        b = [32, 16, 96]

        expected_result = [4, 8, 16]

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)


    def test_6_3_24_36(self):
        a = [6, 2]
        b = [24, 36]

        expected_result = [6, 12]

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)


    def test_3_4_24_48(self):
        a = [3, 4]
        b = [24, 48]

        expected_result = [12, 24]

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)

    def test_single_element_in_a(self):
        a = [5]
        b = [25, 30]

        expected_result = [5]

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)

    def test_large_range(self):
        a = [3, 7]
        b = [210, 420]

        expected_result = [21, 42, 105, 210]

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)

    def test_no_common_numbers(self):
        a = [13, 17]
        b = [40, 60]

        expected_result = []

        actual_result = self.func(a, b)

        self.assertEqual(expected_result, actual_result)

