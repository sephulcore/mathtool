import sys
import math
from calc import equation
from cli import build_parser


parser = build_parser()
args = parser.parse_args()

if args.command is None:
    parser.print_help()
    sys.exit(0)

if args.a is None and args.b is None and args.c is None:
    try:
        a_s = int(input('Введите A:'))
        b_s = int(input('Введите B:'))
        c_s = int(input('Введите C:'))
    except ValueError:
        print('Ошибка: заданный коэффициент не является числом', file=sys.stderr)
        sys.exit(1)
elif args.a is not None and args.b is not None and args.c is not None:
    a_s = args.a
    b_s = args.b
    c_s = args.c
else:
    print('Ошибка: укажите все три коэффициента либо ни одного', file=sys.stderr)
    sys.exit(1)


try:
    a = int(a_s)
    b = int(b_s)
    c = int(c_s)
except ValueError:
    print('Ошибка: заданный коэффициент не является числом', file=sys.stderr)
    sys.exit(1)
try:
    equation.valid_coefs(a, b, c)
except ValueError as error:
    print(f'{error}', file=sys.stderr)
    sys.exit(1)

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