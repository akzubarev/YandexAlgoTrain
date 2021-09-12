if __name__ == '__main__':
    numsdict = dict()
    with open('input.txt', 'r') as fin:
        players = int(fin.readline())
        scores = list(map(int, fin.readline().split()))
        for i in range(len(scores)):
            scores[i] -= scores[-1]
        nums = list(map(int, fin.readline().split()))
        for num in nums:
            if num in numsdict.keys():
                numsdict[num] += 1
            else:
                numsdict[num] = 1

    result = None
    maxcandidates = [num for num in nums if numsdict[num] == 1]
    if len(maxcandidates) == 0:
        result = max(scores[:-1]) + 1
    else:
        maxnum = max(maxcandidates)


        def getresult():
            wins = 0
            result = None
            for key in range(1, maxnum + 1):
                if key not in numsdict.keys():
                    count = 0
                    for score in scores[:-1]:
                        if key > score:
                            count += 1
                    if count > wins:
                        result = key
                        wins = count
                elif numsdict[key] == 1:
                    if result is not None:
                        return result
                    else:
                        for i in range(len(nums)):
                            if nums[i] == key:
                                if scores[i] + key > 0 > scores[i]:
                                    return key
                                else:
                                    if key != 1:
                                        return 1
                                    else:
                                        return 2


        result = getresult()
        if result is None:
            result = maxnum + 1
    print(result)
