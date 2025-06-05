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
    guess_num = n // 2
    while guess(guess_num) != 0:
        if guess(guess_num) == -1:
            guess_num = (0 + guess_num) // 2
        if guess(guess_num) == 1:
            guess_num = (guess_num + n) // 2

    return guess_num

if __name__ == "__main__":
    print(binary_search(10))