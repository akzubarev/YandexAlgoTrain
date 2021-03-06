# Петя нашел на чердаке старый телеграфный аппарат и приделал к нему хитроумное устройство,
# которое может печатать на телеграфной ленте определенное слово (обозначим его X).
# Петино устройство может напечатать на ленте это слово сколько угодно раз.
# Петя может заставить аппарат напечатать на ленте и любое другое сообщение,
# но для этого ему нужно разобрать свое хитроумное устройство, и после этого он уже не сможет печатать сообщение X.
# А самое главное, что напечатать даже один символ другого сообщения потребует от Пети больше усилий,
# чем напечатать на ленте слово X с помощью хитроумного устройства.
# Петя хочет сделать так, чтобы всем казалось, что ему по телеграфу пришло сообщение Z.
# Для этого он может (строго в этой последовательности):
# - сколько угодно раз напечатать сообщение X
# - разобрать хитроумное устройство и посимвольно напечатать еще что-нибудь (назовем это Y)
# - оторвать и выбросить начало ленты так, чтобы на оставшейся ленте было напечатано в точности сообщение Z
# Поскольку набирать отдельные символы сообщения Y довольно сложно, Петя хочет,
# чтобы в сообщении Y было как можно меньше символов.


def read():
    with open('input.txt', 'r') as fin:
        return fin.readline().strip(), fin.readline().strip()


def solve(first, second):
    count = -1
    index = 0

    for i, char in enumerate(reversed(second)):
        if char != first[-1 - index]:
            count = len(second) - i - 1
            index = 0
        else:
            index += 1
            if index == len(first):
                index = 0

    return "" if count == -1 else second[count:]


if __name__ == '__main__':
    print(solve(*read()))
