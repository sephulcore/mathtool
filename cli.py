import argparse

def build_parser():
    parser = argparse.ArgumentParser(prog='mathtool', description='Расчёты над уравнениями и числовыми последовательностями', allow_abbrev=False)
    subparsers = parser.add_subparsers(dest='command')

    solve_parser = subparsers.add_parser('solve', help = 'решение уравнения A*x^2 + B*x + C = 0', allow_abbrev=False)
    solve_parser.add_argument('-a', type=int, help = 'коэффициент A')
    solve_parser.add_argument('-b', type=int, help = 'коэффициент B')
    solve_parser.add_argument('-c', type=int, help = 'коэффициент C')

    stats_parser = subparsers.add_parser('stats', help = 'Показатели последовательности чисел', allow_abbrev=False)
    stats_parser.add_argument('--input', help='Имя файла с числами')

    series_parser = subparsers.add_parser('series', help='сумма числового ряда', allow_abbrev=False)
    series_parser.add_argument('--func', required=True, choices=['sqplus', 'third'], help='какой ряд суммировать')
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--terms', type=int, help='количество слагаемых')
    group.add_argument('--eps', type=float, help='точность вычисления')


    integrate_parser = subparsers.add_parser('integrate', help='численное интегрирование', allow_abbrev=False)
    integrate_parser.add_argument('--func', required=True, choices=['ratio', 'root'], help='какую функцию интегрировать')
    integrate_parser.add_argument('--from', dest='lower', type=float, required=True, help='нижний предел')
    integrate_parser.add_argument('--to', dest='upper', type=float, required=True, help='верхний предел')
    integrate_parser.add_argument('--steps', type=int, required=True, help='количество прямоугольников')
    return parser
