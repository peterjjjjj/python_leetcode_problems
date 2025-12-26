def assign_cookies(g: list[int], s: list[int]) -> int:
    count = 0
    i, j = 0, 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i, j = i + 1, j + 1
        else:
            j += 1

    return count


if __name__ == "__main__":
    print(assign_cookies([1, 2, 3, 4, 5], [1, 2, 3]))
