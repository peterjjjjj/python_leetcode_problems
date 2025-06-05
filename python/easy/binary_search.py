def binary_search(nums: list[int], target: int) -> int:

    lower_bound = 0
    higher_bound = len(nums)-1

    def dfs() -> int:
        nonlocal lower_bound, higher_bound

        if lower_bound > higher_bound:
            return -1

        mid_index = (lower_bound + higher_bound) // 2

        if target == nums[mid_index]:
            return mid_index

        elif target < nums[mid_index]:
            higher_bound = mid_index - 1
            return dfs()

        elif target > nums[mid_index]:
            lower_bound = mid_index + 1
            return dfs()

    return dfs()

if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 12))