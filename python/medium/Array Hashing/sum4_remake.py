#Pointer

def pointer(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    results = []

    for i in range(len(nums) - 3):
        #Skip duplicate, but i > 0 so at least 1 round has completed
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > (i + 1) and nums[j] == nums[j - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    #The increment will break the while loop if they are all the same
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1

                else:
                    right -= 1

    return results

if __name__ == '__main__':
    print(pointer([2,2,2,2,2,2], 8))