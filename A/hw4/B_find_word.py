# def adjacent(pos1, pos2):
#     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1
#
#
# def printTable(used):
#     for i in range(size):
#         line = ""
#         for j in range(size):
#             for char, positions in letters.items():
#                 for pos in positions:
#                     if pos == (i, j):
#                         if used[i][j]:
#                             line += "* "
#                         else:
#                             line += char + " "
#         print(line)
#     print("-" * 10)
#
#
# def solve(remaining_words, letters_coords, used_coords):
#     # print(remaining_words[0])
#     ways = solve_one_word(remaining_words[0], letters_coords, used_coords)
#     # print(len(ways))
#
#     for way in ways:
#         local_used_coords = [used_coords[i].copy() for i in range(len(used_coords))]
#         for pos in way:
#             if len(way) != len(remaining_words[0]) or local_used_coords[pos[0]][pos[1]] == True:
#                 raise Exception(f"{remaining_words[0]} {len(way)} {pos[0]} {pos[1]}\n{way}")
#             local_used_coords[pos[0]][pos[1]] = True
#         # printTable(local_used_coords)
#         if len(remaining_words) > 1:
#             res = solve(remaining_words[1:], letters_coords, local_used_coords)
#             if res is not None:
#                 # if remaining_words[0] == "OOOOOOO":
#                 #     printTable(local_used_coords)
#                 return res
#         else:
#             # printTable(local_used_coords)
#             return local_used_coords
#     return None
#
#
# def solve_one_word(word, letters_coords, used_coords):
#     ways = list()
#     for char in word:
#         found = False
#         possible_pos = letters_coords[char]
#         new_ways = list()
#         for pos in possible_pos:
#             if not used_coords[pos[0]][pos[1]]:
#                 if len(ways) == 0:
#                     new_ways.append([pos])
#                     found = True
#                 else:
#                     for way in ways:
#                         if adjacent(way[-1], pos) and pos not in way:
#                             new_way = way.copy()
#                             new_way.append(pos)
#                             new_ways.append(new_way)
#                             found = True
#         if found:
#             ways = new_ways.copy()
#         else:
#             return []
#
#     res = list()
#     for way in ways:
#         isCopy = False
#         for i in range(len(res)):
#             if set(way) == set(res[i]):
#                 isCopy = True
#                 break
#         if not isCopy:
#             res.append(way)
#
#     # if word == "OOOOOOO":
#     #     for way in ways:
#     #         print(way)
#     #     print("-" * 10)
#     return ways
#
#
# if __name__ == '__main__':
#     letters = dict()
#     with open('input.txt', 'r') as fin:
#         size, wordsnum = map(int, fin.readline().split())
#         words = list()
#         for i in range(size):
#             line = fin.readline().strip()
#             for j in range(size):
#                 if line[j] not in letters.keys():
#                     letters[line[j]] = set()
#                 letters[line[j]].add((i, j))
#         for j in range(wordsnum):
#             words.append(fin.readline().strip())
#
#     used = [[False] * size for _ in range(size)]
#     if wordsnum > 0:
#         used = solve(words, letters, used)
#     remaining = ""
#     for letter in letters.keys():
#         for coords in letters[letter]:
#             if not used[coords[0]][coords[1]]:
#                 remaining += letter
#     print(remaining)
if __name__ == '__main__':
    letters = dict()
    with open('input.txt', 'r') as fin:
        size, wordsnum = map(int, fin.readline().split())
        words = list()
        for _ in range(size):
            line = fin.readline().strip()
            for char in line:
                if char not in letters.keys():
                    letters[char] = 0
                letters[char] += 1

        for _ in range(wordsnum):
            word = fin.readline().strip()
            for char in word:
                letters[char] -= 1

        res = ""
        for letter, num in letters.items():
            if num > 0:
                res += letter * num
        print(res)
