def min_eating_speed(piles: list[int], h: int) -> int:

    sorted_piles = sorted(piles)
    min_bound = sorted_piles[0]
    max_bound = sorted_piles[-1]

    def can_eat_all(speed) -> bool:
        total_time = 0
        for pile in piles:
            time_for_a_pile = pile // speed
            if pile % speed != 0:
                time_for_a_pile += 1

            total_time += time_for_a_pile

        if total_time <= h:
            return True

        return False

    for i in range(min_bound, max_bound):
        if can_eat_all(i):
            return i

if __name__ == '__main__':
    piles = [3,6,7,11]
    print(min_eating_speed(piles, 8))