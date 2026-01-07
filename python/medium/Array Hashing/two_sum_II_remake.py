#Standard two pointers solution.
def two_pointer(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]

        elif nums[left] + nums[right] > target:
            right -= 1

        elif nums[left] + nums[right] < target:
            left += 1

    raise ValueError("No result.")


if __name__ == '__main__':
    print(two_pointer([2,7,11,15], 9))
