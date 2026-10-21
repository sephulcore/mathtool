from calc.arrays import MIN_VALUE, MAX_VALUE

def out_of_order(a, b, descending):
    if descending:
        return a < b
    else:
        return a > b

def bubble(values, descending):
    n = len(values)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if out_of_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if swapped == False:
            break

def selection(values, descending=False):
    n = len(values)
    for i in range(0, n - 1):
        best = i
        for j in range(i + 1, n):
            if out_of_order(values[best], values[j], descending):
                best = j
        values[i], values[best] = values[best], values[i]

def insertion(values, descending=False):
    n = len(values)
    for i in range(1, n):
        current = values[i]
        j = i
        while j > 0 and out_of_order(values[j - 1], current, descending):
            values[j] = values[j - 1]
            j = j - 1
        values[j] = current

def counting(values, descending=False):
    counts = [0] * (MAX_VALUE - MIN_VALUE + 1)
    for value in values:
        counts[value - MIN_VALUE] += 1
    if descending:
        numbers = reversed(range(len(counts)))
    else:
        numbers = range(len(counts))
    k = 0
    for number in numbers:
        for _ in range(counts[number]):
            values[k] = number + MIN_VALUE
            k += 1



METHODS = {
    'bubble': bubble,
    'selection': selection,
    'insertion': insertion,
    'counting': counting
}