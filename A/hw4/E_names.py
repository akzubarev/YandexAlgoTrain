import string

if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        first = fin.readline().strip()
        second = fin.readline().strip()

    firstlettersidx = {n: 0 for n in range(10)}
    startidx1 = 0
    startidx2 = 0
    result = ""
    for char in reversed(string.ascii_lowercase):
        while True:
            idx1 = first.find(char, startidx1)
            idx2 = second.find(char, startidx2)
            if idx1 > -1 and idx2 > -1:
                startidx1 = idx1 + 1
                startidx2 = idx2 + 1
                result += char
            else:
                break

    print(result)
