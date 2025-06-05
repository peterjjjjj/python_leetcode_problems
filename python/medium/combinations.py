def combination(n: int, k: int) -> list[list[int]]:
    """
    O() too complex
    too complex
    :param n:
    :param k:
    :return:
    """
    nums = []
    for i in range(1, n + 1):
        nums.append(i)

    subsets = []
    current_subset = []

    def dfs(index: int) -> None:
        nonlocal current_subset, subsets
        if len(current_subset) == k:
            subsets.append(current_subset[:])
            return

        for i in range(index, n):
            current_subset.append(nums[i])
            dfs(i + 1)
            current_subset.pop()

    dfs(0)
    return subsets

#just to test my understanding of the recursion logic
def permutations(n: int, k: int) -> list[list[int]]:
    nums = []
    for i in range(1, n + 1):
        nums.append(i)

    subsets = []
    current_subset = []


    def dfs(nums: list[int]) -> None:
        nonlocal current_subset, subsets
        #base case
        if len(current_subset) == k:
            subsets.append(current_subset[:])
            return

        for i in range(len(nums)):
            current_subset.append(nums[i])
            dfs(nums[:i] + nums[i + 1:])
            current_subset.pop()

    dfs(nums)

    return subsets



if __name__ == '__main__':
    print(combination(4, 2))
    print(permutations(4, 2))