def canJump(nums: list[int]) -> bool:
    """
    You are given an integer array nums, you are initially positioned at the
    first index in the array represents your max jump length at that position.

    :param nums: list[int]
    :return: boolean
    """

    #Initialize the max length can get to starts at the origin.
    max_length = nums[0]
    #The last index.
    target_index = len(nums) - 1


    for i in range(len(nums) - 1):
        #If the current index is reachable.
        if i <= max_length:
            current_max_length = i + nums[i]
            if current_max_length >= max_length:
                max_length = current_max_length

    return max_length >= target_index


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))
    print(canJump([1]))
    print(canJump([0,2,3]))