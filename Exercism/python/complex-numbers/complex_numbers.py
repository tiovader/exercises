from operator import add, neg
from math import e, cos, sin, sqrt


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    @property
    def __attr(self): return tuple(self.__dict__.values())
    def __repr__(self) -> str: return '%.2f + %.2fi' % (self.__attr)
    def __eq__(self, other: 'ComplexNumber'): return repr(self) == repr(other)
    def __sub__(self, other): return self + neg(other)
    def __neg__(self): return ComplexNumber(-self.real, -self.imaginary)
    def __abs__(self): a, b = self.__attr; return sqrt(a ** 2 + b ** 2)
    def conjugate(self): self.imaginary *= -1; return self

    def __add__(self, other: 'ComplexNumber'):
        self.real += other.real
        self.imaginary += other.imaginary
        return self

    def __mul__(self, other: 'ComplexNumber'):
        a, b, c, d = add(self.__attr, other.__attr)
        self.real = (a * c - b * d)
        self.imaginary = (b * c + a * d)
        return self

    def __truediv__(self, other: 'ComplexNumber'):
        a, b, c, d = add(self.__attr, other.__attr)
        self.real = (a * c + b * d)/(c**2 + d**2)
        self.imaginary = (b * c - a * d)/(c**2 + d**2)
        return self

    def exp(self):
        a, b = self.__attr
        self.real = e ** a * cos(b)
        self.imaginary = e ** a * sin(b)
        return self
