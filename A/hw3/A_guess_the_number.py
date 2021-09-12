if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        num = int(fin.readline())
        line = ""
        answers = set(range(1, num + 1))
        while True:
            line = fin.readline().strip()
            if line == "HELP":
                break
            guess = set(map(int, line.split()))
            guess = answers.intersection(guess)
            if len(guess) <= len(answers) / 2:
                print("NO")
                answers = answers.difference(guess)
            else:
                print("YES")
                answers = guess.copy()
        answers = list(answers)
        answers.sort()
        print(" ".join(map(str, answers)))
