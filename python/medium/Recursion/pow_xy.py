def my_pow(x: float, n: int) -> float:
    """
    LC 50.
    """
    if n == 0:
        return float(1)

    def pow_helper_pos(result: float, power: int) -> float:
        if power == 0:
            return result

        result = result * x
        power -= 1

        return pow_helper_pos(result, power)

    def pow_helper_neg(result: float, power: int) -> float:
        if power == 0:
            return 1 / result

        result = result * x
        power += 1

        return pow_helper_neg(result, power)

    if n > 0:
        return pow_helper_pos(x, n)

    return pow_helper_neg(x, n)

if __name__ == '__main__':
    print(my_pow(5.0, 2))
    print(my_pow(5.0, -2))