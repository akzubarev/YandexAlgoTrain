# Последовательность состоит из натуральных чисел и завершается числом 0.
# Всего вводится не более 10000 чисел (не считая завершающего числа 0).
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
# Числа, следующие за числом 0, считывать не нужно.

if __name__ == '__main__':

    max = 0
    count = 0
    with open('input.txt', 'r') as fin:
        while True:
            num = int(fin.readline())
            if num > max:
                max = num
                count = 1
            elif num == max:
                count += 1
            if num == 0:
                break

    print(count)
