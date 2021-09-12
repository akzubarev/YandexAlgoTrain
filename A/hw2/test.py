import unittest

from A.hw2.B_tel import solve


class TestA(unittest.TestCase):

    # def test_A_their(self):
    #     self.assertEqual(2, solve(2, -4, 7, 1))
    #     self.assertEqual("NO", solve(1, 1, 2, 2))
    #     self.assertEqual("NO", solve(35, 14, 11, -3))
    #
    # def test_A_my(self):
    #     self.assertEqual("NO", solve(1, 1, 2, 2))
    #     self.assertEqual("INF", solve(0, 0, 0, 1))
    #     self.assertEqual("INF", solve(0, 0, 0, 1))
    #     self.assertEqual("NO", solve(0, 2, 0, 1))

    # def test_A_their(self):
    #     self.assertEqual("YES", solve((1, 1, 4, 2, 3, 0, 2, 3)))
    #     self.assertEqual("NO", solve((1, 1, 5, 2, 2, 3, 3, 0)))
    #     self.assertEqual("YES", solve((0, 0, 5, 1, 6, 3, 1, 2)))
    #
    # def test_A_my(self):
    #    pass

    # def test_C_their(self):
    #     self.assertEqual("NO", solve([1, 1, 1],
    #                                  [1, 1, 1],
    #                                  [1, 1, 1]))
    #     self.assertEqual("YES", solve([2, 1, 1],
    #                                   [1, 1, 2],
    #                                   [2, 2, 1]))
    #     self.assertEqual("YES", solve([1, 1, 1],
    #                                   [2, 0, 2],
    #                                   [0, 0, 0]))
    #     self.assertEqual("YES", solve([0, 0, 0],
    #                                   [0, 1, 0],
    #                                   [0, 0, 0]))
    #
    # def test_C_my(self):
    #     self.assertEqual("NO", solve([1, 1, 1],  # два игрока победили  одновременно
    #                                  [2, 2, 2],
    #                                  [0, 0, 0]))
    #     self.assertEqual("NO", solve([1, 1, 1],  # три победы одновременно
    #                                  [2, 2, 2],
    #                                  [1, 1, 1]))
    #     self.assertEqual("YES", solve([1, 1, 1],  # один игрок победил 2 раза
    #                                   [1, 2, 2],
    #                                   [1, 2, 2]))
    #     self.assertEqual("YES", solve([1, 1, 1],  # то же самое но по другому
    #                                   [2, 1, 2],
    #                                   [1, 2, 2]))
    #     self.assertEqual("NO", solve([1, 2, 1],  # один игрок походил больше другого
    #                                  [2, 1, 2],
    #                                  [2, 2, 0]))
    #     self.assertEqual("NO", solve([0, 0, 0],  # второй игрок походил раньше первого
    #                                  [0, 2, 0],
    #                                  [0, 0, 0]))
    #     self.assertEqual("YES", solve([0, 0, 0],  # никто не ходил
    #                                   [0, 0, 0],
    #                                   [0, 0, 0]))
    #     self.assertEqual("YES", solve([1, 2, 1],  # две диагональных победы
    #                                   [2, 1, 2],
    #                                   [1, 2, 1]))
    #     self.assertEqual("NO", solve([1, 0, 1],  # победил 2 игрок, а 1 походил на 1 раз больше
    #                                  [0, 1, 1],
    #                                  [2, 2, 2]))
    #     self.assertEqual("NO", solve([1, 1, 1],  # победил 1 игрок, а 2 походил столько же раз
    #                                  [0, 2, 0],
    #                                  [2, 0, 2]))

    # def test_A_their(self):
    #     self.assertEqual(7, solve(4, 2, [45, 52, 47, 46]))
    #
    # def test_A_my(self):
    #     for _ in range(10):
    #         n = random.randint(3, 20)
    #         lst = list()
    #         for i in range(n):
    #             lst.append(random.randint(0, 20))
    #         _min = min(lst)
    #         _max = max(lst)
    #         iterations = random.randint(1, 10)
    #         for i in range(iterations):
    #             s = sum(lst)
    #             lst = [s - l for l in lst]
    #         self.assertEqual(_max - _min, solve(n, iterations, lst))

    def test_B_their(self):
        self.assertEqual("m", solve("mama", "amamam"))
        self.assertEqual("mura", solve("ura", "mura"))
        self.assertEqual("comp", solve("computer", "comp"))
        self.assertEqual("", solve("ejudge", "judge"))
        self.assertEqual("", solve("m", "mmm"))

    def test_B_my(self):
        pass


if __name__ == '__main__':
    unittest.main()
