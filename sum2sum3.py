

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
            indices = []
            indices.append(nums.index(sorted_nums[i]))
            for k in range(len(nums)):
                if sorted_nums[j] == nums[k] and k not in indices:
                    indices.append(k)
            return indices
        elif sum > target:
            j=j-1
        elif sum < target:
            i=i+1
    return False

def threeSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]

def threeSum2(nums, target):
    nums.sort()
    for i in range(0, len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            sum = nums[j] + nums[k]
            if sum == target - nums[i]:
                return nums[i], nums[j], nums[k]
            elif sum > target - nums[i]:
                k = k-1
            elif sum < target - nums[i]:
                j=j+1
        return False


nums = [3,3]
print(twoSum(nums, 12))
print(twoSum2(nums, 6))
print(threeSum(nums, 12))
print(threeSum2(nums, 12))