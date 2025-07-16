def canJump(nums: list[int]) -> bool:
    """
    You are given an integer array nums, you are initially positioned at the
    first index in the array represents your max jump length at that position.

    :param nums: list[int]
    :return: boolean
    """

    max_length = set()
    target_index = len(nums) - 1

    for i in range(len(nums)):
        current_max_length = i + nums[i]
        max_length.add(current_max_length)

    return True if target_index in max_length else False

if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))