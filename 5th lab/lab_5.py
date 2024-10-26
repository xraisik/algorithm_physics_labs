import unittest
from typing import Self
from math import sqrt

class Complex:
    def __init__(self, _re: float = 0., _im: float = 0.) -> None:
        self.__re = _re
        self.__im = _im

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}*i"

    @property
    def real(self) -> float:
        return self.__re

    @real.setter
    def real(self, val: float) -> None:
        self.__re = val

    # Same for properties for imaginary part
    @property
    def imaginary(self) -> float:
        return self.__im

    @imaginary.setter
    def imaginary(self, val: float) -> None:
        self.__im = val

    # Dunder methods
    def __add__(self, other: Self) -> Self: # c1 + c2
        return Complex(self.__re + other.real, self.__im + other.imaginary)

    def __iadd__(self, other: Self) -> Self: # c1 += c2
        self.__re += other.real
        self.__im += other.imaginary

        return self

    def __sub__(self, other: Self) -> Self: # c1 - c2
        return Complex(self.__re - other.real, self.__im - other.imaginary)

    def __isub__(self, other: Self) -> Self:
        self.__re -= other.real
        self.__im -= other.imaginary

        return self

    def __mul__(self, other: Self) -> Self: # c1 * c2
        re = self.__re * other.real - self.__im * other.imaginary
        im = self.__re * other.imaginary + self.__im * other.real

        return Complex(re, im)

    def __imul__(self, other: Self) -> Self:
        temp_re = self.__re * other.real - self.__im * other.imaginary
        temp_im = self.__re * other.imaginary + self.__im * other.real

        self.__re = temp_re
        self.__im = temp_im

        return self

    def __truediv__(self, other: Self) -> Self:  # c1 / c2
        re = (self.__re * other.real + self.__im * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        im = (self.__im * other.real - self.__re * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)

        return Complex(re, im)

    def __itruediv__(self, other: Self) -> Self:
        temp_re = (self.__re * other.real + self.__im * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        temp_im = (self.__im * other.real - self.__re * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)

        self.__re = temp_re
        self.__im = temp_im

        return self

    def __abs__(self) -> Self:
        return sqrt(self.__re ** 2 + self.__im ** 2)

    def __eq__(self, other: Self) -> bool: # c1 == c2
        return self.__re == other.real and self.__im == other.imaginary

    def __ne__(self, other: Self) -> bool: # c1 != c2
        return not self == other

class TestComplex(unittest.TestCase):
    def setUp(self):
        self.c1 = Complex(1., 2.)
        self.c2 = Complex(2., 3.)
        self.c3 = Complex(-1., -1.)

    def test_add(self):
        result = self.c1 + self.c2
        self.assertEqual(result.real, 3.0)
        self.assertEqual(result.imaginary, 5.0)

    def test_iadd(self):
        self.c1 += self.c2
        self.assertEqual(self.c1.real, 3.0)
        self.assertEqual(self.c1.imaginary, 5.0)

    def test_sub(self):
        result = self.c1 - self.c2
        self.assertEqual(result.real, -1.0)
        self.assertEqual(result.imaginary, -1.0)

    def test_isub(self):
        self.c1 -= self.c2
        self.assertEqual(self.c1.real, -1.0)
        self.assertEqual(self.c1.imaginary, -1.0)

    def test_mul(self):
        result = self.c1 * self.c2
        self.assertEqual(result.real, -4.0)
        self.assertEqual(result.imaginary, 7.0)

    def test_imul(self):
        self.c1 *= self.c2
        self.assertEqual(self.c1.real, -4.0)
        self.assertEqual(self.c1.imaginary, 7.0)

    def test_truediv(self):
        result = self.c1 / self.c2
        self.assertEqual(round(result.real, 3), 0.615)
        self.assertEqual(round(result.imaginary, 3), 0.077)

    def test_itruediv(self):
        self.c1 /= self.c2
        self.assertEqual(round(self.c1.real, 3), 0.615)
        self.assertEqual(round(self.c1.imaginary, 3), 0.077)

    def test_abs(self):
        result = abs(self.c1)
        self.assertEqual(round(result, 3), 2.236)

    def test_eq(self):
        self.assertTrue(self.c1 == Complex(1., 2.))
        self.assertFalse(self.c1 == self.c2)

    def test_ne(self):
        self.assertTrue(self.c1 != self.c2)
        self.assertFalse(self.c1 != Complex(1., 2.))

    def test_str(self):
        self.assertEqual(str(self.c1), "1.0 + 2.0*i")
        self.assertEqual(str(self.c3), "-1.0 + -1.0*i")

if __name__ == "__main__":
    unittest.main()