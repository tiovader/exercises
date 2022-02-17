from __future__ import division
from fractions import Fraction


class Rational:
    def __init__(self, numer: int, denom: int):
        def gcd():
            a, b = abs((numer)), abs(denom)
            if a == b:
                return a

            r = 1, (min(a, b) + 1)
            return max(
                {div for div in range(*r) if a % div == 0}
                .intersection({div for div in range(*r) if b % div == 0}))

        self.numer = numer//gcd() if abs(numer) >= 1 and denom > 0 \
            else -numer//gcd() if denom < 0 else 0
        self.denom = abs(denom)//gcd() if abs(numer) >= 1 else 1

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer
        elif isinstance(other, (int, float)):
            return self.numer / self.denom == other
        else:
            return False

    def __repr__(self):
        return str(self.numer / self.denom) if self.numer % self.denom == 0 \
            else '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Rational):
            self.numer = \
                (self.numer * other.denom) + (self.denom * other.numer)
            self.denom = self.denom * other.denom
        elif isinstance(other, (int, float)):
            other = Fraction(other)
            self += Rational(other.numerator, other.denominator)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: \
                '{type(self).__name__}' and '{type(other).__name__}'")

        return Rational(self.numer, self.denom)

    def __sub__(self, other):
        if isinstance(other, Rational):
            return self.__add__(Rational(-(other.numer), other.denom))
        elif isinstance(other, (int, float)):
            return self.__add__(-other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: \
                '{type(self).__name__}' and '{type(other).__name__}'")

    def __mul__(self, other):
        if isinstance(other, Rational):
            self.numer *= other.numer
            self.denom *= other.denom

        elif isinstance(other, (int, float)):
            other = Fraction(other)
            self *= Rational(other.numerator, other.denominator)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: \
                '{type(self).__name__}' and '{type(other).__name__}'")
        return Rational(self.numer, self.denom)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            self *= Rational(other.denom if other.numer >
                             0 else -other.denom, abs(other.numer))
        elif isinstance(other, (int, float)):
            other = Fraction(other)
            self *= Rational(other.denominator, other.numerator)
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: \
                '{type(self).__name__}' and '{type(other).__name__}'")
        return Rational(self.numer, self.denom)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    def __pow__(self, power):
        if isinstance(power, Rational):
            aux = Fraction(self.numer ** power)
            self.numer = aux.numerator
            self.denom = aux.denominator
        elif isinstance(power, int):
            if power > 0:
                self.numer **= power
                self.denom **= power
            else:
                self.numer = self.denom ** abs(power)
                self.denom = self.numer ** abs(power)
        elif isinstance(power, float):
            power = Fraction(power)
            self **= Rational(power.numerator, power.denominator)

        return Rational(self.numer, self.denom)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)
