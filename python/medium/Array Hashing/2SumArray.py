def twoSum(nums, target):
    """
    O(n) is array sorted
    O(1) space complexity
    """
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1, j+1]
        elif nums[i] + nums[j] > target:
            j -= 1
            continue
        elif nums[i] + nums[j] < target:
            i += 1
            continue
        return False

if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))
