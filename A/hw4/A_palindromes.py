if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        num = int(fin.readline())
        line = fin.readline().strip()

    letters = dict()
    for char in line:
        if char in letters.keys():
            letters[char] += 1
        else:
            letters[char] = 1

    keys = list(letters.keys())
    keys.sort()
    firsthalf = ""
    secondhalf = ""
    middle = ""
    for key in keys:
        while letters[key] > 1:
            firsthalf = firsthalf + key
            secondhalf = key + secondhalf
            letters[key] -= 2
        if letters[key] == 1 and len(middle) == 0:
            middle = key

    res = f"{firsthalf}{middle}{secondhalf}"
    if len(res) == 0:
        res = keys[0]
    print(res)
