# Пусть A — массив, состоящий из N элементов A1,…,AN.
# Обозначим его максимальное и минимальное значение через max(A) и min(A) соответственно.
# Вычислим сумму элементов S, S=A1+A2+…+AN. Заменим каждый элемент массива на разницу S и этого элемента:
# Такое преобразование массива A назовем операцией Confuse. Напишите программу, которая по массиву B,
# полученному в результате K-кратного применения операции Confuse к некоторому массиву A,
# вычислит разность max(A)-min(A)


def read():
    with open('input.txt', 'r') as fin:
        num, iterations = map(int, fin.readline().split())
        lst = list(map(int, fin.readline().split()))
        return num, iterations, lst


def solve(num, iterations, lst):
    # # Sn = Sn-1 * len(lst)-1
    # min = lst[0]
    # max = lst[0]
    # # sum = 0
    #
    # for l in lst:
    #     if l > max:
    #         max = l
    #     if l < min:
    #         min = l
    #     # sum += l

    # for _ in range(iterations):
    #     print(f"{max} {min}")
    #     sum = int(sum / (num - 1))
    #     max =  sum - max
    #     min =  sum - min
    # print(f"---{max} {min}-----")

    return abs(max(lst) - min(lst))


if __name__ == '__main__':
    print(solve(*read()))
