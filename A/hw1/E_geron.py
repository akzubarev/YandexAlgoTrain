# Среди треугольников периметра P с целыми длинами сторон
# найдите треугольник наибольшей и наименьшей ненулевой площади.

def max_S(P: int):
    if P != 3 and P < 5:
        return -1

    third_of_P = int(P / 3)
    remain = P / 3 - third_of_P
    if remain > 0.5:
        a = third_of_P + 1
        b = third_of_P + 1
        c = third_of_P
    elif remain > 0:
        a = third_of_P + 1
        b = third_of_P
        c = third_of_P
    else:
        a = b = c = third_of_P
    return f"{a} {b} {c}"


def min_S(P: int):
    a = 1
    b = int(P / 2) + 1
    c = P - b - a
    while a + c <= b:
        b -= 1
        c += 1
        if a + b <= c:
            a += 1
            c -= 1
    return f"{a} {b} {c}"


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        P = int(fin.readline())
    if P != 3 and P < 5:
        print(-1)
    else:
        print(max_S(P))
        print(min_S(P))
