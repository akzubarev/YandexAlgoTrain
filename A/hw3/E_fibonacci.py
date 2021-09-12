def is_fib(n: int):
    pass


if __name__ == '__main__':
    with open('input.txt', 'r') as fin:
        num = int(fin.readline())
        for i in range(num):
            print(is_fib(int(fin.readline())))
