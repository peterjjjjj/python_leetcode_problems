def fibonacci(n: int) -> int:
    memo = {}
    def calculation(n: int) -> int:
        nonlocal memo
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
            return n

        result = calculation(n - 1) + calculation(n - 2)
        memo[n] = result
        return result

    return calculation(n)

if __name__ == '__main__':
    print(fibonacci(3))
