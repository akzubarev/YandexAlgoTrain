# Из шахматной доски по границам клеток выпилили связную
# (не распадающуюся на части) фигуру без дыр. Требуется определить ее периметр.

if __name__ == '__main__':
    P = 0
    lst = list()
    with open('input.txt', 'r') as fin:
        num = int(fin.readline())
        for _ in range(num):
            x, y = map(int, fin.readline().split())
            P += 4
            for x_1, y_1 in lst:
                if x_1 == x and abs(y - y_1) == 1 \
                        or y_1 == y and abs(x - x_1) == 1:
                    P -= 2
            lst.append((x, y))
    print(P)
