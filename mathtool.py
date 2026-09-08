import sys
args = sys.argv[1:]
if len(args) == 0 or args[0] == '--help':  # Вывод справки
    print('mathtool - решение уравнений вида A*x^2 + B*x + C = 0')
    sys.exit(0)
if args[0] != 'solve':  # Неизвестная комана(не solve)
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