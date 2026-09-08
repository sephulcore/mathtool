import sys
args = sys.argv[1:]
if len(args) == 0 or args[0] == '--help':  # Вывод справки
    print('mathtool - решение уравнений вида A*x^2 + B*x + C = 0')
    sys.exit(0)
if args[0] != 'solve':  # Неизвестная комана(не solve)
    print(f'Ошибка:неизвестная команда', file=sys.stderr)
    sys.exit(1)