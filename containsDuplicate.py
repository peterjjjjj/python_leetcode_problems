
def containsDuplicate(nums):
    num_set = set()
    duplicate_set = set()
    for num in nums:
        if num not in num_set:
            num_set.add(num)
        else:
            duplicate_set.add(num)

    return duplicate_set

if __name__ == '__main__':
    set = containsDuplicate([1, 2, 3, 1])
    print(set)

