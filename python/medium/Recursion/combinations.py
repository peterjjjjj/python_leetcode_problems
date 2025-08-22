def combine(n: int, k: int) -> list[list[int]]:
    """
    LC 77.
    """

    all_combinations = []

    def dfs(combination: list[int], current_num: int) -> None:
        combination.append(current_num)

        #Basecase, append copy to all_combinations.
        if len(combination) == k:
            all_combinations.append(combination[:])
            return

        for i in range(current_num + 1, n + 1):
            dfs(combination, i)
            combination.pop()

    for i in range(1, n + 1):
        dfs([], i)

    return all_combinations

if __name__ == '__main__':
    print(combine(1,1))
