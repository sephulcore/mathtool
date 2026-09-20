import argparse

def build_parser():
    parser = argparse.ArgumentParser(prog='mathtool', description='Расчёты над уравнениями и числовыми последовательностями', allow_abbrev=False)
    subparsers = parser.add_subparsers(dest='command')

    solve_parser = subparsers.add_parser('solve', help = 'решение уравнения A*x^2 + B*x + C = 0', allow_abbrev=False)
    solve_parser.add_argument('-a', type=int, help = 'коэффициент A')
    solve_parser.add_argument('-b', type=int, help = 'коэффициент B')
    solve_parser.add_argument('-c', type=int, help = 'коэффициент C')
    return parser
