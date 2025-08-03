from itertools import combinations


def combination_sum_2(candidates: list[int], target: int) ->list[list[int]]:
    """
    Given collection of nums in candidates, find all unique combinations in candidates where candidate numbers sum to target.


    """

    all_combinations = list()
    #Sort the list.
    candidates.sort()

    def dfs(current_index: int, current_sum: int, combination: list[int]) -> None:
        if current_sum == target:
            all_combinations.append(combination[:])
            return

        if current_sum > target:
            return

        for i in range(current_index, len(candidates)):

            if current_sum + candidates[i] > target:
                break

            if i > current_index and candidates[i] == candidates[i - 1]:
                continue


            combination.append(candidates[i])

            dfs(i + 1, current_sum + candidates[i], combination)
            combination.pop()


    dfs(0, 0, [])

    return all_combinations



if __name__ == '__main__':
    print(combination_sum_2([10,1,2,7,6,1,5], 8))