def combination_sum(
        candidates: list[int],
        target: int) -> list[list[int]]:

    """
    Given an array of distinct integers candidates and a target integer target.

    Find all unique combinations of candidates that sum to target.

    :param candidates: list of unique integers
    :param target: integer
    :return: list of combinations of candidates that sum to target
    """

    combinations = []

    def dfs(current_index, remaining_target: int, current_combination = []) -> None:
        nonlocal combinations
        if remaining_target == 0:
            combinations.append(current_combination[:])
            return

        if remaining_target < 0:
            return

        for i in range(current_index, len(candidates)):
            if candidates[i] > remaining_target:
                break

            current_combination.append(candidates[i])
            dfs(i, remaining_target - candidates[i], current_combination)
            current_combination.pop()


    dfs(0, target)

    return combinations

if __name__ == '__main__':
    print(combination_sum([2,3], 6))
