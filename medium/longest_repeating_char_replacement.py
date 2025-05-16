def longest_repeating_char_replacement(s, k):

    """

    :param s:
    :param k:
    :return:

    tc = O(n)
    sc = O(n)
    """

    current_char = dict()
    left = 0
    right = 0
    current_max_freq = 0
    max_freq = 0


    for i in range(len(s)):
        right = i
        if s[i] not in current_char:
            current_char[s[i]] = 1
        else:
            current_char[s[i]] += 1

        if current_char[s[i]] >= current_max_freq:
            current_max_freq = current_char[s[i]]

        while right - left + 1 - current_max_freq > k:
            current_char[s[left]] -= 1
            left += 1

        max_freq = max(right - left + 1, max_freq)

    return max_freq

if __name__ == '__main__':
    print(longest_repeating_char_replacement('BADEB', 2))