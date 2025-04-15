

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]

def twoSum2(nums, target):
    sorted_nums = sorted(nums)
    i=0
    j=len(nums)-1
    while i<j:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum == target:
            return sorted_nums[i], sorted_nums[j]
        elif sum > target:
            j=j-1
        elif sum < target:
            i=i+1
    return False

nums = [2, 7, 11, 15]
print(twoSum(nums, 13))
print(twoSum2(nums, 13))