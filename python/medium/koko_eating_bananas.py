def min_eating_speed(piles: list[int], h: int) -> int:

    sorted_piles = sorted(piles)
    min_bound = 0
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


    while min_bound <= max_bound:
        mid = (min_bound + max_bound) // 2
        if can_eat_all(mid):
            if not can_eat_all(mid - 1):
                return mid
            else:
                max_bound = mid - 1
        else:
            if can_eat_all(mid + 1):
                return mid + 1
            else:
                min_bound = mid + 1

if __name__ == '__main__':
    piles = [312884470]
    print(min_eating_speed(piles, 312884469))