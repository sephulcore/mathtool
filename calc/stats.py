import math
def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError('последовательность пуста')
    if len(numbers) > 20:
        raise ValueError('последовательность больше 20-ти чисел')
    for number in numbers:
        if number is not math.isfinite(number):
            raise ValueError('недопустимое значение')
        if abs(number) > 10000:
            raise ValueError('значение вне допустимого диапазона')
