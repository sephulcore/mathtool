import random
MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000
def fill(count, low = MIN_VALUE, high = MAX_VALUE, seed = None):
    random.seed(seed)
    values = []
    for _ in range(count):
        values.append(random.randint(low, high))
    return values
def valid_fill(count, low, high):
    if count < 1 or count > MAX_VALUE:
        raise ValueError('количество аргументов вне допустимого диапазона')
    if low > high:
        raise ValueError('нижняя граница выше верхней')
    if low < MIN_VALUE or high > MAX_VALUE:
        raise ValueError('границы значений вне диапазона')