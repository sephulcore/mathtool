from calc import arrays

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

METHODS = {'bubble': bubble}