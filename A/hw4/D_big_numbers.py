if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        first = fin.readline().strip()
        second = fin.readline().strip()

    firstnumbers = {n: 0 for n in range(10)}
    secondnumbers = {n: 0 for n in range(10)}

    for char in first:
        firstnumbers[int(char)] += 1
    for char in second:
        secondnumbers[int(char)] += 1

    res = ""
    for i in reversed(range(0, 10)):
        res += f"{i}" * min(firstnumbers[i], secondnumbers[i])

    if len(res) == 0:
        print(-1)
    elif res[0] == "0":
        print(0)
    else:
        print(res)
