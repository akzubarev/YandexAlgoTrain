# На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм.
# На перемене после урока они стали играть в игру: Петя называл координаты четырех точек в произвольном порядке,
# а Вася должен был ответить, являются ли эти точки вершинами параллелограмма.
# Вася, если честно, не очень понял тему про параллелограммы, и ему требуется программа,
# умеющая правильно отвечать на Петины вопросы.
# Напомним, что параллелограммом называется четырехугольник, противоположные стороны которого равны и параллельны.

def read() -> list[map]:
    with open('input.txt', 'r') as fin:
        num = int(fin.readline())
        lsts = list()
        for i in range(num):
            lsts.append(map(int, fin.readline().split()))
        return lsts


def solve(lst: map):
    xa, ya, xb, yb, xc, yc, xd, yd = lst
    xAB = xa - xb
    yAB = ya - yb
    xCD = xd - xc
    yCD = yd - yc

    xAC = xa - xc
    yAC = ya - yc
    xCB = xd - xb
    yCB = yd - yb

    if (xAB == xCD and yAB == yCD) or \
            (xAB == -xCD and yAB == -yCD) or \
            (xAC == xCB and yAC == yCB) or \
            (xAC == -xCB and yAC == -yCB):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    for lst in read():
        print(solve(lst))
