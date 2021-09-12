# На Новом проспекте построили подряд 10 зданий.
# Каждое здание может быть либо жилым домом, либо магазином, либо офисным зданием.
# Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко приходится идти до ближайшего магазина.
# Для разработки плана развития общественного транспорта на Новом проспекте мэр города попросил вас выяснить,
# какое же наибольшее расстояние приходится преодолевать жителям Нового проспекта,
# чтобы дойти от своего дома до ближайшего магазина.


if __name__ == '__main__':

    max_dist = 0
    last_shop_idx = -1
    right_house_idx = 0
    left_house_idx = -1

    with open('input.txt', 'r') as fin:
        lst = list(map(int, fin.readline().split()))

    houses = list()
    for i, num in enumerate(lst):
        if num == 1:
            houses.append(i)

        elif num == 2:
            if last_shop_idx == -1:
                candidates = [i - house_idx for house_idx in houses]
            else:
                candidates = [min(house_idx - last_shop_idx, i - house_idx) for house_idx in houses]
            candidates.append(max_dist)
            max_dist = max(candidates)

            houses = list()
            last_shop_idx = i

    if len(houses) != 0:
        candidates = [house_idx - last_shop_idx for house_idx in houses]
        candidates.append(max_dist)
        max_dist = max(candidates)

    print(max_dist)
