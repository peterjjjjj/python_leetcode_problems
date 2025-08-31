def ways_to_compute_recursion(expression: str) -> list[int]:
    """
    LC 241.
    """

    memo = {}

    def compute(expression: str) -> list[int]:
        nonlocal memo

        if expression in memo:
            return memo[expression]

        if expression.isdigit():
            return [int(expression)]

        results = []

        for i in range(len(expression) - 1):
            if expression[i] in "+-*":
                left_result = compute(expression[:i])
                right_result = compute(expression[i + 1:])

                for left in left_result:
                    for right in right_result:
                        if expression[i] == '+':
                            results.append(left + right)
                        elif expression[i] == '*':
                            results.append(left * right)
                        elif expression[i] == '-':
                            results.append(left - right)

        memo[expression] = results
        return results

    return compute(expression)

def ways_to_compute_dp(expression: str) -> list[int]:

    nums = []
    signs = []

    temp = ''

    for i in range(len(expression)):
        if expression[i].isdigit():
            temp += expression[i]
        else:
            signs.append(expression[i])
            nums.append(int(temp))
            temp = ''

    dp = [[[] for _ in range(len(nums))] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][i] = [nums[i]]

    pass
    #Not yet done


if __name__ == '__main__':
    #print(ways_to_compute_recursion('1+2*3'))
    print(ways_to_compute_recursion('2-1-1'))
