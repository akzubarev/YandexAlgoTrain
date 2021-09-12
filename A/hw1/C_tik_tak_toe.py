# Напишите программу, которая по изображению поля для игры в «Крестики-нолики» определит,
# могла ли такая ситуация возникнуть в результате игры с соблюдением всех правил.
# Напомним, что игра в «Крестики-нолики» ведется на поле 3*3. Два игрока ходят по очереди.
# Первый ставит крестик, а второй – нолик. Ставить крестик и нолик разрешается в любую еще не занятую клетку поля.
# Когда один из игроков поставит три своих знака в одной горизонтали, вертикали или диагонали,
# или когда все клетки поля окажутся заняты, игра заканчивается.


def read() -> list[list]:
    with open('input.txt', 'r') as fin:
        rows = list()
        for i in range(3):
            rows.append(list(map(int, fin.readline().split())))
        return rows


def solve(firstrow: list, secondrow: list, thirdrow: list):
    vertical_wins = list()
    horizontal_wins = list()
    diagonal_wins = list()

    for column in range(3):
        if firstrow[column] != 0 and firstrow[column] == secondrow[column] == thirdrow[column]:
            vertical_wins.append(firstrow[column])

    for row in firstrow, secondrow, thirdrow:
        if row[0] != 0 and row[0] == row[1] == row[2]:
            horizontal_wins.append(row[0])

    if secondrow[1] != 0 and firstrow[0] == secondrow[1] == thirdrow[2]:
        diagonal_wins.append(secondrow[1])
    if secondrow[1] != 0 and firstrow[2] == secondrow[1] == thirdrow[0]:
        diagonal_wins.append(secondrow[1])

    if len(vertical_wins) > 1 or len(horizontal_wins) > 1:  # or len(diagonal_wins) > 1:
        return "NO"

    wins = list()
    wins.extend(horizontal_wins)
    wins.extend(vertical_wins)
    wins.extend(diagonal_wins)

    if len(wins) > 0:
        if len(wins) > 2 or (len(wins) == 2 and wins[0] != wins[1]):
            return "NO"

    field = list()
    field.extend(firstrow)
    field.extend(secondrow)
    field.extend(thirdrow)

    countX = field.count(1)
    countO = field.count(2)

    if countX - countO > 1 or \
            countO > countX or \
            (len(wins) > 0 and wins[0] == 2 and countX > countO) or \
            (len(wins) > 0 and wins[0] == 1 and countX == countO):
        return "NO"

    return "YES"


if __name__ == '__main__':
    field = read()
    print(solve(field[0], field[1], field[2]))
