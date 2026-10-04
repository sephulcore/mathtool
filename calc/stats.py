import math
MAX_VALUE = 10000
MAX_COUNT = 20

def check_number(number):
    if not math.isfinite(number):
        raise ValueError('недопустимое значение')
    if abs(number) > MAX_VALUE:
        raise ValueError('значение вне допустимого диапазона')

def validate_numbers(numbers):
    """Проверяет список чисел: непустой, не длиннее MAX_COUNT, все конечные и в диапазоне."""
    if len(numbers) == 0:
        raise ValueError('последовательность пуста')
    if len(numbers) > MAX_COUNT:
        raise ValueError('последовательность больше 20-ти чисел')
    for number in numbers:
        if not math.isfinite(number):
            raise ValueError('недопустимое значение')
        if abs(number) > MAX_VALUE:
            raise ValueError('значение вне допустимого диапазона')
        
def total(numbers):
    """Возвращает сумму чисел в списке."""
    result = 0
    for number in numbers:
        result += number
    return result

def mean(numbers):
    """Возвращает среднее арифметическое чисел в списке."""

    return total(numbers) / len(numbers)

def sum_squares(numbers):
    """Возвращает сумму квадратов чисел в списке."""
    result = 0
    for number in numbers:
        result += number ** 2
    return result

def square_mean(numbers):
    """Возвращает среднее квадратическое чисел в списке."""
    return math.sqrt(sum_squares(numbers) / len(numbers))

def sum_square_deviation(numbers):
    """Возвращает сумму квадратов отклонений чисел от их среднего."""
    avg = mean(numbers)
    result = 0
    for number in numbers:
        result += (number - avg) ** 2
    return result

def var(numbers):
    """Возвращает дисперсию чисел в списке."""  
    return sum_square_deviation(numbers) / len(numbers)

def square_otkl(numbers):
    """Возвращает СКО (корень из дисперсии) чисел в списке."""
    return math.sqrt(var(numbers))

def st_deviation(numbers):
    """Возвращает стандартное отклонение, или None, если чисел меньше двух."""
    if len(numbers) < 2:
        return None
    return math.sqrt(sum_square_deviation(numbers) / (len(numbers) - 1))

def minimum(numbers):
    """Возвращает наименьшее число в списке."""
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result

def maximum(numbers):
    """Возвращает наибольшее число в списке."""
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result

def count_plus(numbers):
    """Возвращает количество положительных чисел в списке."""
    result = 0
    for number in numbers:
        if number > 0:
            result += 1
    return result

def count_minus(numbers):
    """Возвращает количество отрицательных чисел в списке."""
    result = 0
    for number in numbers:
        if number < 0:
            result += 1
    return result

itog = [
    ('Сумма', total, '.3f'),
    ('Ср. арифм.', mean, '.3f'),
    ('Сумма кв.', sum_squares, '.3f'),
    ('Ср. кв.', square_mean, '.3f'),
    ('Дисперсия', var, '.3f'),
    ('СКО', square_otkl, '.3f'),
    ('Станд. откл.', st_deviation, '.3f'),
    ('Наименьшее', minimum, '.3f'),
    ('Наибольшее', maximum, '.3f'),
    ('Положительных', count_plus, 'd'),
    ('Отрицательных', count_minus, 'd'),
]


