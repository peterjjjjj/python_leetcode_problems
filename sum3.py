def threeSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]

def threeSum2(nums, target):
    nums.sort()
    indices = []
    for i in range(0, len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            sum = nums[j] + nums[k]
            if sum == target - nums[i]:
                if [nums[i], nums[j], nums[k]] not in indices:
                    indices.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif sum > target - nums[i]:
                k = k-1
            elif sum < target - nums[i]:
                j=j+1
    return indices

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums, 0))
print(threeSum2(nums, 0))