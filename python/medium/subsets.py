def subsets_recursion(nums: list[int]) -> list[list[int]]:
    """
    O(N*2^N) copy takes N,
    O(N*2^N)
    :param nums:
    :return:
    """
    current_subset = []
    results = []

    def dfs(index: int) -> None:
        nonlocal current_subset, results

        results.append(current_subset[:])

        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            dfs(i + 1)

            current_subset.pop()


    dfs(0)

    return results

def subsets_bit(nums: list[int]) -> list[list[int]]:
    """
    O(N*N^2)
    O(N*N^2)
    :param nums:
    :return:
    """
    n = len(nums)
    total_subsets = 1 << n

    subsets = []

    for i in range(total_subsets):
        current_subset = []
        for j in range(n):
            if i & (1 << j):
                current_subset.append(nums[j])

        subsets.append(current_subset)

    return subsets

def subsets2(nums: list[int]) -> list[list[int]]:
    subsets = []
    current_subset = []

    def dfs(index: int) -> None:
        nonlocal current_subset, subsets

        subsets.append(current_subset[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            current_subset.append(nums[i])
            dfs(i + 1)
            current_subset.pop()

    dfs(0)
    return subsets

if __name__ == '__main__':
    #print(subsets_recursion([1, 2, 3]))
    #print(subsets_bit([1, 2, 3]))
    print(subsets2([1, 2, 2]))

