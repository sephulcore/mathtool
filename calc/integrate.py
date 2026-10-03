import math
MAX_STEPS = 100000

def func_ratio(x):
    return x / (x+1)

def func_root(x):
    return math.sqrt(x * x + 1)

def valid_steps(steps):
    if steps < 1 or steps > MAX_STEPS:
        raise ValueError('количество прямоугольников вне диапазона')

FUNCTIONS = {
    'ratio': (func_ratio, 'F(x) = x / (x + 1)', 0, 20, True),
    'root': (func_root, 'F(x) = sqrt(x^2 + 1)', -5, 5, False)
}

def integrate(func, a, b, steps):
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += func(x) * dx
    return result

def valid_bounds(a, b, low, high, inclusive):
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError('предел должен быть конечным числом')
    if a >= b:
        raise ValueError('левая граница должна быть меньше правой')
    if inclusive:
        if a < low or a > high or b < low or b > high:
            raise ValueError('предел  вне промежутка')
    else:
        if a <= low or a >= high or b <= low or b >= high:
            raise ValueError('предел вне промежутка')
        