if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        _, numofpairs = map(int, fin.readline().split())
        line = fin.readline().strip()
        lefts = dict()
        rights = dict()
        for i in range(numofpairs):
            pair = fin.readline().strip()
            lefts[pair[0]] = 0
            if pair[1] not in rights.keys():
                rights[pair[1]] = list()
            rights[pair[1]].append(pair[0])

    result = 0
    for char in line:
        if char in rights.keys():
            for left in rights[char]:
                result += lefts[left]
                # print(left, char, lefts[left])
        if char in lefts.keys():
            lefts[char] += 1
    print(result)
