import math
import fractions

def find_largest_x_for_pell_equation(limit):
    return max((n for n in range(2, limit + 1) if not is_square(n)), key=find_minimal_x)

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

def find_minimal_x(n):
    continued_fraction = convert_to_continued_fraction(n)
    terms = continued_fraction[0] + continued_fraction[1][:-1]
    
    value = fractions.Fraction(terms[-1], 1)
    for term in reversed(terms[:-1]):
        value = 1 / value + term
    
    if len(continued_fraction[1]) % 2 == 0:
        return value.numerator
    else:
        return value.numerator**2 + value.denominator**2 * n

def convert_to_continued_fraction(n):
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        floor_val = val.floor()
        terms.append(floor_val)
        val = (val - QuadraticSurd(floor_val, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
    split = seen[val]
    return (terms[:split], terms[split:])

class QuadraticSurd:
    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()
        
        if c < 0:
            a = -a
            b = -b
            c = -c
        gcd = math.gcd(a, b, c)
        if gcd != 1:
            a //= gcd
            b //= gcd
            c //= gcd
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d)

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d)

    def floor(self):
        temp = math.isqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d

    def __hash__(self):
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)

limit = 1000
result = find_largest_x_for_pell_equation(limit)
print(result)