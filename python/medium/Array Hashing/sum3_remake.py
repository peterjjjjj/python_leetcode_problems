#3 pointers solution

def three_pointer(nums: list[int]) -> list[list[int]]:
    #Sort nums
    nums.sort()
    results = []

    for i in range(len(nums) - 2):
        #Skip the same value for i to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        #If current num > 0, all nums after it are +, cant add to 0
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                results.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right:
                    if nums[left] == nums[left + 1]:
                        left += 1
                    if nums[right] == nums[right - 1]:
                        right -= 1

            #Move left
            elif current_sum < 0:
                left += 1

            #Move right
            else:
                right -= 1

    return results


if __name__ == '__main__':
    print(three_pointer([-1,0,1,2,-1,-4]))