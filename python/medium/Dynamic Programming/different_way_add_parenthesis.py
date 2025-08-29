def ways_to_compute_recursion(expression: str) -> list[int]:
    """
    LC 241.
    """

    memo = {}

    results = []

    def compute(expression: str) -> int:
        nonlocal results, memo

        if expression in memo:
            return memo[expression]

        if expression.isdigit():
            return int(expression)

        result = 0

        for i in range(0, len(expression) - 1):
            char = expression[i]

            if char in "+-*":
                left = compute(expression[:i])
                right = compute(expression[i+1:])

                if char == '+':
                    result = (left + right)
                    memo[expression] = result
                elif char == '*':
                    result = (left * right)
                    memo[expression] = result
                elif char == '-':
                    result = (left - right)
                    memo[expression] = result

        memo[expression] = result
        results.append(result)
        return result

    compute(expression)
    return results

if __name__ == '__main__':
    print(ways_to_compute_recursion('1+2*3'))
