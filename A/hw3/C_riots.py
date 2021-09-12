if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        days, parties = map(int, fin.readline().split())
        riots = set()
        for i in range(parties):
            start, frequency = map(int, fin.readline().split())
            riots = riots.union(set(range(start, days + 1, frequency)))

    saturdays = set(range(6, days + 1, 7))
    sundays = set(range(7, days + 1, 7))
    riots = riots.difference(saturdays).difference(sundays)
    print(len(riots))
