import sys
import math
args = sys.argv[1:]
if len(args) == 0 or args[0] == '--help':
    print('mathtool — консольное приложение для решения алгебраических уравнений вида A*x^2 + B*x + C = 0,\n'
        'где A, B, C — коэффициенты уравнения, задаваемые пользователем.\n'
        'Приложение вычисляет и выводит действительные корни уравнения.\n'
        '\n'
        'Способы запуска:\n'
        '  python mathtool.py                          — вывод справки\n'
        '  python mathtool.py --help                    — вывод справки\n'
        '  python mathtool.py solve                      — ввод коэффициентов с клавиатуры\n'
        '  python mathtool.py solve -a 1 -b -3 -c 2      — решение с заданными коэффициентами\n'
        '\n'
        'Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.')
    sys.exit(0)

if args[0] != 'solve':  
    print(f'Ошибка:неизвестная команда', file=sys.stderr)
    sys.exit(1)

if len(args) == 1:
    a_s = input('Введите A:')
    b_s = input('Введите B:')
    c_s = input('Введите C:')
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
    print('Ошибка: коэффициент не является целым числом', file=sys.stderr)
    sys.exit(1)
if abs(a) > 10_000 or abs(b) > 10_000 or abs(c) > 10_000:
     print('Ошибка: значение вне допустимого диапазона', file=sys.stderr)
     sys.exit(1)

if a == 0:
    if b != 0:
        print('Уравнение линейное')
        x = -c / b
        print(f'x = {x:.3f}')
    else:
        print('Ошибка: это не уравнение', file=sys.stderr)
        sys.exit(1)
else:
    print('Уравнение квадратное')
    d = b * b - 4 * a * c
    print(f'D = {d}')
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'x1 = {x1:.3f}')
        print(f'x2 = {x2:.3f}')
    elif d == 0:
        x = -b / (2 * a)
        print(f'x = {x:.3f}')
    else:
        print('Действительных корней нет')