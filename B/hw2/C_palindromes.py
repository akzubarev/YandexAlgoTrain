# В строкоремонтную мастерскую принесли строку, состоящую из строчных латинских букв.
# Заказчик хочет сделать из неё палиндром. В мастерской могут за 1 байтландский тугрик
# заменить произвольную букву в строке любой выбранной заказчиком буквой.
# Какую минимальную сумму придётся заплатить заказчику за ремонт строки?
# Напомним, что палиндромом называется строка, которая равна самой себе, прочитанной в обратном направлении.

if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        word = fin.readline().strip()

    res = 0
    for i in range(int(len(word) / 2)):
        if word[i] != word[-1 - i]:
            res += 1

    print(res)
