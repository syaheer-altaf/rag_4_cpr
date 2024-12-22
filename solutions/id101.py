from fractions import Fraction

DEGREE = 10

def lagrange_interpolation(points, x_value):
    result = Fraction(0)
    for i, (xi, yi) in enumerate(points):
        term = Fraction(yi)
        for j, (xj, _) in enumerate(points):
            if i != j:
                term *= Fraction(x_value - xj, xi - xj)
        result += term
    return result

def generate_sequence_values(limit):
    return [sum((-n)**i for i in range(DEGREE + 1)) for n in range(1, limit + 1)]

sequence_values = generate_sequence_values(DEGREE + 1)
total_fit_sum = Fraction(0)

for k in range(1, DEGREE + 1):
    points = [(n, sequence_values[n - 1]) for n in range(1, k + 1)]
    for n in range(k + 1, DEGREE + 2):
        predicted = lagrange_interpolation(points, n)
        actual = sequence_values[n - 1]
        if predicted != actual:
            total_fit_sum += predicted
            break

numerator, denominator = total_fit_sum.numerator, total_fit_sum.denominator
result = str(numerator) if denominator == 1 else f"{numerator}/{denominator}"
print(result)