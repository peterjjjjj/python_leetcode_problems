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

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            #Move left
            elif current_sum < 0:
                left += 1

            #Move right
            else:
                right -= 1

    return results


def practice(nums: list[int]) -> list[list[int]]:
    nums.sort()
    results = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                results.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                #Make sure to review this logic
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            if current_sum < 0:
                left += 1
            else:
                right -= 1

    return results

if __name__ == '__main__':
    #print(three_pointer([-1,0,1,2,-1,-4]))
    print(three_pointer([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
    print(practice([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))