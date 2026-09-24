import math
MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITER = 100000

def chet(n):
    if n % 2 == 0:
        return -1
    return 1

def term_sqplus(n):
    return chet(n) / (n * n + 1)

def term_third(n):
    return chet(n) / (n * 3)

FORMULAS = {
    'sqplus': (term_sqplus,'S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ...'),
    'third': (term_third, 'S = 1/3 - 1/6 + 1/9 - ...'),
}

def sum_by_term(term, count):
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result

def sum_by_eps(term, eps):
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
    if terms < 1 or terms > MAX_TERMS:
        raise ValueError('количество слагаемых вне диапазона')

def validate_eps(eps):
    if not math.isfinite(eps) or eps <= 0 or eps > MAX_EPS:
        raise ValueError('точность вне диапазона')