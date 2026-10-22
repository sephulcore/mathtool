import sys
import time
from calc import equation
from calc import stats
from calc import series
from calc import integrate
from calc import arrays
from calc import sorting
from cli import build_parser

def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        try:
            a_s = int(input('Введите A:'))
        except ValueError:
            raise ValueError('заданный коэффициент не является числом')
        equation.check_range('A', a_s)
        try:
            b_s = int(input('Введите B:'))
        except ValueError:
            raise ValueError('заданный коэффициент не является числом')
        equation.check_range('B', b_s)
        try:
            c_s = int(input('Введите C:'))
        except ValueError:
            raise ValueError('заданный коэффициент не является числом')
        equation.check_range('C',c_s)
    elif args.a is not None and args.b is not None and args.c is not None:
        a_s = args.a
        b_s = args.b
        c_s = args.c
    else:
        raise ValueError('укажите все три коэффициента либо ни одного')


    try:
        a = int(a_s)
        b = int(b_s)
        c = int(c_s)
    except ValueError:
        raise ValueError('заданный коэффициент не является числом')
    equation.valid_coefs(a, b, c)

    kind, d, roots = equation.solve(a, b, c)
    if kind == "линейное":
        print('Уравнение линейное')
        print(f'x = {roots[0]:.3f}')
    else:
        print('Уравнение квадратное')
        print(f'Дискриминант: {d}')
        if len(roots) == 2:
            print(f'x1 = {roots[0]:.3f}')
            print(f'x2 = {roots[1]:.3f}')
        elif len(roots) == 1:
            print(f'x = {roots[0]:.3f}')
        else:
            print('Действительных корней нет')
    return 0

def handle_stats(args):
    if args.input:
        with open(args.input, encoding = 'utf-8-sig') as handle:
            numbers = read_numbers(handle)
    else:
        numbers = []
        print('Введите числа:')
        while True:
            text = input()
            if text == "":
                break
            numbers.extend(text.split())
        numbers = read_numbers(numbers)


    stats.validate_numbers(numbers)
    print(f'Количество: {len(numbers)}')
    for lab, func, form in stats.itog:
        value = func(numbers)
        if value is None:
            print(f'{lab}: не существует')
        else:
            print(f'{lab}: {value:{form}}')
    return 0

def read_numbers(source):
    numbers = []
    for line in source:
        for word in line.split():
            try:
                number = float(word)
            except ValueError:
                raise ValueError(f'{word} не является числом')
            stats.check_number(number)
            numbers.append(number)
    return numbers

def handle_series(args):
    term, formula = series.FORMULAS[args.func]

    if args.terms is not None:
        series.validate_terms(args.terms)
        result = series.sum_by_term(term, args.terms)
        count = args.terms
    else:
        series.validate_eps(args.eps)
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f'Слагаемых: {count}')
    print(f'Сумма ряда: {result:.4f}')
    return 0

def handle_integrate(args):
    func, formula, low, high, inclusive = integrate.FUNCTIONS[args.func]

    integrate.valid_bounds(args.lower, args.upper, low, high, inclusive)
    integrate.valid_steps(args.steps)

    print(formula)
    result = integrate.integrate(func, args.lower, args.upper, args.steps)
    print(f'Значение интеграла: {result:.4f}')
    return 0

def read_array(path=None):
    if path:
        with open(path, encoding="utf-8-sig") as file:
            text = file.read()
    else:
        print("Введите числа:", file=sys.stderr)
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line.strip():
                break
            lines.append(line)
        text = " ".join(lines)
    text = text.replace(",", " ")
    words = text.split()
    values = []
    for word in words:
        try:
            value = int(word)
        except ValueError:
            raise ValueError(f'{word} не является числом')
        values.append(value)
    if len(values) < 1:
        raise ValueError('Необходимо ввести хотя бы одно число')
    if len(values) > arrays.MAX_COUNT:
        raise ValueError('Количество чисел превышает максимально допустимое')
    for value in values:
        if value < arrays.MIN_VALUE or value > arrays.MAX_VALUE:
            raise ValueError(f'Число {value} выходит за допустимый диапазон')
    return values

def write_array(path, values):
    with open(path, "w", encoding="utf-8") as file:
        file.write(" ".join(str(x) for x in values)+ "\n")

def handle_fill(args):
    arrays.valid_fill(args.count, args.min, args.max)
    array = arrays.fill(args.count, args.min, args.max, args.seed)
    if args.output:
        write_array(args.output, array)
        print(f'Записано элементов: {len(array)} в файл {args.output}')
    else:
        print(" ".join(str(x) for x in array))
    return 0

def handle_sort(args):
    array = read_array(args.input)
    method = sorting.METHODS[args.method]
    measure(f'sort({args.method})', method, [array, args.order == 'desc'])
    method(array, args.order == 'desc')
    if args.output:
        write_array(args.output, array)
        part = f'Записано элементов: {len(array)} в файл {args.output}'
    else:
        part = ' '.join(str(x) for x in array)
    print(part + '; Массив отсортирован.')
    return 0

def handle_search(args):
    if abs(args.value) > arrays.MAX_SEARCH:
        raise ValueError('модуль искомого больше максимального значения')
    values = read_array(args.input)
    if not arrays.is_ascending(values):
        raise ValueError('массив не отсортирован по возрастанию')
    index = arrays.binary_search(values, args.value)
    if index is None:
        print(f'Значение {args.value} не найдено')
        return 1
    print(f'Значение {args.value} имеет элемент с индексом {index + 1}')
    return 0

def measure(name, oper, parameters):
    begin = time.perf_counter()
    result = oper(*parameters)
    elapsed = time.perf_counter() - begin
    print(f'Время операции {name}: {elapsed:.6f} с', file=sys.stderr)
    return result    
def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0
    try:
        if args.command == 'solve':
            return handle_solve(args)
        elif args.command == 'stats':
            return handle_stats(args)
        elif args.command == 'series':
            return handle_series(args)
        elif args.command == 'integrate':
            return handle_integrate(args)
        elif args.command == 'fill':
            return handle_fill(args)
        elif args.command == 'sort':
            return handle_sort(args)
        elif args.command == 'search':
            return handle_search(args)
    except (ValueError,OSError) as error:
        print(f'Ошибка: {error}', file = sys.stderr)
        return 1
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))