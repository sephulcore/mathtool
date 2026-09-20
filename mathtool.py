import sys
import math
from calc import equation
from cli import build_parser


parser = build_parser()
args = parser.parse_args()

if args.command is None:
    parser.print_help()
    sys.exit(0)


if len(args) == 1:
    try:
        a_s = int(input('Введите A:'))
    except ValueError:
        print('Ошибка: заданный коэффициент не является числом',file=sys.stderr)
        sys.exit(1)
    try:
            b_s = int(input('Введите B:'))
    except ValueError:
        print('Ошибка: заданный коэффициент не является числом',file=sys.stderr)
        sys.exit(1)
    try:
        c_s = int(input('Введите C:'))
    except ValueError:
        print('Ошибка: заданный коэффициент не является числом', file=sys.stderr)
        sys.exit(1)
elif len(args) == 7 and args[1] == '-a' and args[3] == '-b' and args[5] == '-c':
    a_s = args[2]
    b_s = args[4]
    c_s = args[6]

else:
    print('Ошибка: неверный набор параметров', file=sys.stderr)
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