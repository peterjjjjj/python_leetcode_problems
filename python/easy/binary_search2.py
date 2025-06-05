#leetcode 374 guess number higher or lower, API defined, -1 for num > pick, 1 for num < pick, 0 for num == pick

def guess(num: int) -> int:
    #6 as testcase
    if num < 6:
        return 1
    if num > 6:
        return -1
    if num == 6:
        return 0

def binary_search(n: int) -> int:
    low_bound = 1
    high_bound = n

    while low_bound <= high_bound:
        mid = (low_bound + high_bound) // 2

        result = guess(mid)

        if result == 0:
            return mid

        elif result == 1:
            low_bound = mid + 1

        elif result == -1:
            high_bound = mid - 1



if __name__ == "__main__":
    print(binary_search(10))