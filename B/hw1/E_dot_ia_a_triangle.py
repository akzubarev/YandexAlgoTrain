# На координатной плоскости расположены равнобедренный прямоугольный треугольник ABC с длиной катета d и точка X.
# Катеты треугольника лежат на осях координат, а вершины расположены в точках: A (0,0), B (d,0), C (0,d).
# Напишите программу, которая определяет взаимное расположение точки X и треугольника.
# Если точка X расположена внутри или на сторонах треугольника, выведите 0.
# Если же точка находится вне треугольника, выведите номер ближайшей к ней вершины.


import math


def read() -> (int, int, int):
    with open('input.txt', 'r') as fin:
        return int(fin.readline()), *map(int, fin.readline().split())


def dist(xfrom, yfrom, xto, yto):
    return math.sqrt((xfrom - xto) ** 2 + (yfrom - yto) ** 2)


if __name__ == '__main__':
    d, x, y = read()

    if 0 <= y <= d and 0 <= x <= d and y <= d - x:
        res = 0
    else:
        dist1 = dist(0, 0, x, y)
        dist2 = dist(d, 0, x, y)
        dist3 = dist(0, d, x, y)

        res = 1
        if dist2 < dist1:
            res = 2
        if dist3 < dist1 and dist3 < dist2:
            res = 3

    print(res)
