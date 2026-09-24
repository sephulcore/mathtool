import math
MAX_VALUE = 10000
MAX_COUNT = 20
def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError('последовательность пуста')
    if len(numbers) > 20:
        raise ValueError('последовательность больше 20-ти чисел')
    for number in numbers:
        if not math.isfinite(number):
            raise ValueError('недопустимое значение')
        if abs(number) > 10000:
            raise ValueError('значение вне допустимого диапазона')
        
def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def mean(numbers):
    return total(numbers) / len(numbers)

def sum_squares(numbers):
    result = 0
    for number in numbers:
        result += number ** 2
    return result

def quadrat_mean(numbers):
    return math.sqrt(sum_squares(numbers) / len(numbers))

def sum_square_deviation(numbers):
    avg = mean(numbers)
    result = 0
    for number in numbers:
        result += (number - avg) ** 2
    return result

def var(numbers):
    return sum_square_deviation(numbers) / len(numbers)

def square_otkl(numbers):
    return math.sqrt(var(numbers))

def st_deviation(numbers):
    if len(numbers) < 2:
        return None
    return math.sqrt(sum_square_deviation(numbers) / (len(numbers) - 1))

def minimum(numbers):
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result
def maximum(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result

def count_plus(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += 1
    return result

def count_minus(numbers):
    result = 0
    for number in numbers:
        if number < 0:
            result += 1
    return result

itog = [
    ('Сумма', total, '.3f'),
    ('Ср. арифм.', mean, '.3f'),
    ('Сумма кв.', sum_squares, '.3f'),
    ('Ср. кв.', quadrat_mean, '.3f'),
    ('Дисперсия', var, '.3f'),
    ('СКО', square_otkl, '.3f'),
    ('Станд. откл.', st_deviation, '.3f'),
    ('Наименьшее', minimum, '.3f'),
    ('Наибольшее', maximum, '.3f'),
    ('Положительных', count_plus, 'd'),
    ('Отрицательных', count_minus, 'd'),
]


