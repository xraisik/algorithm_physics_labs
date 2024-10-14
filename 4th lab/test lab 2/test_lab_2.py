import unittest


class TestWeightsEquilibrium(unittest.TestCase):
    def setUp(self) -> None:
        self.func = self._buildTestedFunction()
    @staticmethod
    def _buildTestedFunction():
        from lab_2 import weights_equilibrium
        return weights_equilibrium

    def test_empty_list(self):
        # Arrange
        initial_weights = []
        expected_equilibrium = -1

        # Act
        actual_equilibrium = self.func(initial_weights)

        # Assert
        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_no_equilibrium(self):
        # Arrange
        initial_weights = [6, 6, 9]
        expected_equilibrium = -1

        # Act
        actual_equilibrium = self.func(initial_weights)

        # Assert
        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_equilibrium_43_51_35_4(self):
        # Arrange
        initial_weights = [43, 51, 35, 4]
        expected_equilibrium = 1

        # Act
        actual_equilibrium = self.func(initial_weights)

        # Assert
        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_equilibrium_big_list(self):
        # Arrange
        initial_weights = [19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]
        expected_equilibrium = 7

        # Act
        actual_equilibrium = self.func(initial_weights)

        # Assert
        self.assertEqual(expected_equilibrium, actual_equilibrium)

    def test_equilibrium_7_24_3_38(self):
        # Arrange
        initial_weights = [7, 24, 3, 38]
        expected_equilibrium = 2

        # Act
        actual_equilibrium = self.func(initial_weights)

        # Assert
        self.assertEqual(expected_equilibrium, actual_equilibrium)