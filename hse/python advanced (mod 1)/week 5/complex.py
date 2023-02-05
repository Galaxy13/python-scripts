from math import sqrt

class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        """
        re: int, float
        im: int, float
        """
        if isinstance(re, (int, float)) and isinstance(im, (int, float)):
            self.re = re
            self.im = im
            self.sign = '+' if self.im >= 0 else ''
        else:
            raise TypeError('re and im should be int or float')

    def __str__(self) -> str:
        return str(self.re) + self.sign + str(self.im) + 'i'

    # Part 2
    def __add__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except AttributeError:
            return Complex(self.re + other, self.im)

    def __sub__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        try:
            return Complex(self.re - other.re, self.im - other.im)
        except AttributeError:
            return Complex(self.re - other, self.im)

    # Part 3
    def __mul__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        try:
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        except AttributeError:
            return Complex(self.re * other, self.im * other)

    def __truediv__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        try:
            return Complex((other.re * self.re + other.im * self.im) / (other.re ** 2 + other.im ** 2),
                           (other.re * self.im - self.re * other.im) / (other.re ** 2 + other.im ** 2))
        except (AttributeError, ZeroDivisionError):
            return Complex(other * self.re / other ** 2, self.im * other / other ** 2)

    # Part 4
    def __eq__(self, other) -> bool:
        """
        other: Complex
        """
        try:
            return self.re == other.re and self.im == other.im
        except AttributeError:
            return self.re == other and not self.im

    def __abs__(self) -> float:
        return sqrt(self.re ** 2 + self.im ** 2)