def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        #if the left half is sorted
        if nums[mid] >= nums[left]:
            #the target is in the left half
            if nums[mid] >= target >= nums[left]:
                right = mid
            #the target is in the right half
            else:
                left = mid
        #the right half is sorted
        elif nums[mid] <= nums[right]:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid

    return -1

if __name__ == '__main__':
    test_nums = [4,5,6,7,0,1,2]
    print(search(test_nums, 3))