def permutations(nums: list[int]) -> list[list[int]]:
    """
    O(N*N!) N factorial, size of all combinations, N from the copy
    O(N*N!)
    :param nums:
    :return:
    """
    all_permutations = []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        first = nums[i]
        rest = nums[:i] + nums[i+1:]

        rest = permutations(rest)

        for p in rest:
            all_permutations.append([first] + p)

    return all_permutations

if __name__ == '__main__':
    print(permutations([1, 2, 3]))