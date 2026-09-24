import math

MAX_VALUE = 10_000
def check_range(name, value):
    if abs(value) > MAX_VALUE:
        raise ValueError(f'коэффициент {name} вне допустимого диапазона')
def valid_coefs(a, b, c):
    coefficients = {"A": a, "B": b, "C": c}
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f'коэффициент {name} вне допустимого диапазона')
    if a == 0 and b == 0:
        raise ValueError('это не уравнение, неизвестное отсутствует')

def solve(a, b, c):
    if a == 0:
        if b != 0:
            x = -c / b
            return "линейное", None, [x]
    else:
        d = b * b - 4 * a * c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return "квадратное", d, [x1, x2]
        elif d == 0:
            x = -b / (2 * a)
            return "квадратное", d, [x]
        else:
            return "квадратное", d, []