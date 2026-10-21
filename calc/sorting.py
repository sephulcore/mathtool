from calc import arrays

METHODS = {}

def out_of_order(a, b, descending):
    if descending:
        return a < b
    else:
        return a > b