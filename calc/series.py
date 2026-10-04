import math
MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITER = 100000

def chet(n):
    """Возвращает знак n-го слагаемого: -1 для чётных n, 1 для нечётных."""
    if n % 2 == 0:
        return -1
    return 1

def term_sqplus(n):
    """Возвращает n-е слагаемое ряда sqplus: ±1/(n^2+1)."""
    return chet(n) / (n * n + 1)

def term_third(n):
    """Возвращает n-е слагаемое ряда third: ±1/(3n)."""
    return chet(n) / (n * 3)

FORMULAS = {
    'sqplus': (term_sqplus,'S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ...'),
    'third': (term_third, 'S = 1/3 - 1/6 + 1/9 - ...'),
}

def sum_by_term(term, count):
    """Суммирует count первых слагаемых ряда term."""   
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result

def sum_by_eps(term, eps):
    """Суммирует слагаемые ряда term, пока очередное не станет меньше eps по модулю."""
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITER:
            raise ValueError('точность не достигнута')


def validate_terms(terms):
    """Проверяет на количество слагаемых."""
    if terms < 1 or terms > MAX_TERMS:
        raise ValueError('количество слагаемых вне диапазона')

def validate_eps(eps):
    """Проверяет на точность."""
    if not math.isfinite(eps) or eps <= 0 or eps > MAX_EPS:
        raise ValueError('точность вне диапазона')