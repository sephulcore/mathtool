import sys
from calc import equation
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
        numbers = read_numbers(sys.stdin)
    print(numbers)
    return 0

def read_numbers(source):
    numbers = []
    for line in source:
        for word in line.split():
            try:
                number = float(word)
            except ValueError:
                raise ValueError(f'{word} не является числом')
            numbers.append(number)
    return numbers

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
    except (ValueError,OSError) as error:
        print(f'Ошибка: {error}', file = sys.stderr)
        return 1
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))