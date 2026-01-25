def search(nums: list[int], target: int) -> int:
    """
    O(log n)
    O(1)
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        #if the left half is sorted
        if nums[mid] >= nums[left]:
            #the target is in the left half
            if nums[mid] >= target >= nums[left]:
                right = mid - 1
            #the target is in the right half
            else:
                left = mid + 1
        #the right half is sorted
        elif nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def practice(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        #The order in this part is correct, left to mid
        if nums[mid] >= nums[left]:
            #And target is in this part
            if nums[mid] >= target >= nums[left]:
                right = mid #Ask Gemini why this works
            else:
                left = mid + 1

        elif nums[mid] < nums[right]:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    test_nums = [4,5,6,0,1,2]
    test_1 = [1,2,3,4,5,0]
    print(search(test_nums, 0))
    print(search(test_1, 3))
    print(practice(test_nums, 0))
    print(practice(test_1, 3))