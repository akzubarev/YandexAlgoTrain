# Витя работает недалеко от одной из станций кольцевой линии Московского метро,
# а живет рядом с другой станцией той же линии.
# Требуется выяснить, мимо какого наименьшего количества промежуточных станций необходимо проехать Вите по кольцу,
# чтобы добраться с работы домой.

def read() -> (int, int, int):
    with open('input.txt', 'r') as fin:
        return map(int, fin.readline().split())


if __name__ == '__main__':
    N, i, j = read()
    res = min(
        abs(i - j) - 1,  # по часовой
        abs(i + N - j) - 1,  # против, j слева от N
        abs(j + N - i) - 1  # против, i слева от N
    )
    print(res)
