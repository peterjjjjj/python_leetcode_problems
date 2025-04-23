def fourSum(nums, target):
    sorted_nums = sorted(nums)
    indices = []
    for i in range(0, len(sorted_nums)-3):
        for j in range(i+1, len(sorted_nums)-2):
            k = j+1
            x = len(sorted_nums)-1
            while k < x:
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k] + sorted_nums[x]
                if sum == target:
                    if [sorted_nums[i], sorted_nums[j], sorted_nums[k], sorted_nums[x]] not in indices:
                        indices.append([sorted_nums[i], sorted_nums[j], sorted_nums[k], sorted_nums[x]])
                    k += 1
                    x -= 1
                elif sum < target:
                    k += 1
                elif sum > target:
                    x -= 1

    return indices

nums = [1,0,-1,0,-2,2]
print(fourSum(nums, 0))

