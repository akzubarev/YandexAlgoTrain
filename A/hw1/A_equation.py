# Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0

def read() -> (int, int, int, int):
    with open('input.txt', 'r') as fin:
        a = int(fin.readline())
        b = int(fin.readline())
        c = int(fin.readline())
        d = int(fin.readline())

        return a, b, c, d


def solve(a, b, c, d):
    if a != 0 and b % a != 0:
        return "NO"

    if a == 0:
        if b != 0:
            return "NO"  # N/(cx+d) = 0
        else:
            return "INF"  # 0/(cx+d) = 0
    else:
        if c != 0 and b / a == d / c:
            return "NO"  # 0/0
        else:
            return int(-b / a)  # ok


if __name__ == '__main__':
    res = solve(*read())
    print(res)
