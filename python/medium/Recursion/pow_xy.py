def my_pow(x: float, n: int) -> float:
    """
    LC 50.
    """
    if n == 0:
        return float(1)

    def pow_helper(result: float, power: int) -> float:
        if power == 0:
            return 1.0

        if power % 2 == 0:
            return pow_helper(result * result, power // 2)

        else:
            return result * pow_helper(result * result, (power - 1) // 2)


    if n > 0:
        return pow_helper(x, n)

    else:
        return 1 / pow_helper(x, -n)


if __name__ == '__main__':
    print(my_pow(2.0, 4))
    print(my_pow(2.0, -4))
