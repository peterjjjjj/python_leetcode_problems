def max_cookies(g: list[int], s: list[int]) -> int:
    """

    :param g: list[int]
    :param s: list[int]
    :return: int
    """

    if not g or not s:
        return 0

    i = 0
    count = 0

    for j in range(len(g)):
        if s[i] >= g[j]:
            count += 1
            i += 1
            if i >= len(s):
                break

    return count

if __name__ == "__main__":
    print(max_cookies([1,2,3], [3]))
