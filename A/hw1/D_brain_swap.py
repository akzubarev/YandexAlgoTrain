# В очередной серии Футурамы было проведено несколько обменов разумами между телами героев, но,
# по крайней мере Бубльгум Тэйт и Сладкий Клайд в обменах не участвовали.
# Теперь необходимо вернутьразумы всех героев в свои тела. К сожалению, два тела могут участвовать только в одном
# обмене,поэтому обратные обмены для этого произвести невозможно. Например, если тело 1поменялось разумом с телом 2,
# а потом тело 1 поменялось разумом с телом 3,то в теле 1 находится разум третьего героя,
# в теле 2 - разум первого героя,а в теле 3 - второго. Теперь можно произвести обмен разумами только между телами 2 и 3,
# тогда разум второго героя вернется в свое тело, а первому и третьему героям могут помочь только Тэйт с Клайдом.
# Помогите героям Футурамы вернуться в свои тела.

def read():
    with open('input.txt', 'r') as fin:
        n, swaps = map(int, fin.readline().split())

        body = [i for i in range(n + 1)]
        for i in range(swaps):
            _from, _to = map(int, fin.readline().split())
            body[_from], body[_to] = body[_to], body[_from]
    return body, n


if __name__ == "__main__":
    body, n = read()

    def swap(a, b):
        print(a, b)
        body[a], body[b] = body[b], body[a]
        return body[b]


    for i in range(1, n - 2):
        if body[i] != i:
            now = i
            while body[body[n - 1]] != i:
                now = swap(now, n - 1)

            swap(now, n)
            swap(now, n - 1)
            swap(body[n], n)
    if body[n - 1] == n:
        swap(n - 1, n)
