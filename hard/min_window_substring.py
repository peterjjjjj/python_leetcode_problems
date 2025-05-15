def min_window_brute(s, t):
    t_freq = dict()
    min_length = len(s)
    min_found_substring = ""

    if not t:
        return ''

    for char in t:
        if char not in t_freq:
            t_freq[char] = 1
        else:
            t_freq[char] += 1

    for i in range(len(s)):
        for j in range(i, len(s)):
            current_sub = s[i:j + 1]

            if len(current_sub) >= min_length:
                continue

            current_freq = dict()
            for char_in_sub in current_sub:
                if char_in_sub in current_freq:
                    current_freq[char_in_sub] += 1
                else:
                    current_freq[char_in_sub] = 1

            is_valid_window = True
            for char_t, freq_t in t_freq.items():
                if current_freq.get(char_t, 0) < freq_t:
                    is_valid_window = False
                    break
            if is_valid_window:
                if len(current_sub) < min_length:
                    min_length = len(current_sub)
                    min_found_substring = current_sub

            return min_found_substring

    return min_found_substring

def min_window(s, t):
    """

    :param s: string
    :param t: target substring
    :return:

    left = pointer to left bound of the current substring
    right = pointer to right bound of the current substring
    min_length = the length of the minimum substring
    substring_start = the start of the substring
    substring_end = the end of the substring
    num_unique_char = num of unique characters needs to be found
    """


    left = 0
    right = 0
    min_length = float('inf')
    substring_start = 0
    substring_end = 0
    remaining_t = len(t)

    substring = dict()
    t_freq = dict()
    for char in t:
        if char not in t_freq:
            t_freq[char] = 1
        else:
            t_freq[char] += 1


    for i in range(len(s)):
        right = i
        current_char = s[right]

        if current_char in t_freq:
            if current_char in substring:
                substring[current_char] += 1
            else:
                substring[current_char] = 1

            if substring[current_char] <= t_freq[current_char]:
                remaining_t -= 1

            if remaining_t == 0:
                while True:
                    if s[left] in t_freq:
                        if substring[s[left]] == t_freq[s[left]]:
                            left += 1
                            substring[s[left - 1]] -= 1
                            remaining_t += 1
                            break
                        substring[s[left]] -= 1

                        left += 1

                #move left back to the valid substring
                left -= 1


                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    substring_start = left
                    substring_end = right

    return s[substring_start:substring_end+1] if min_length != float('inf') else ''

if __name__ == '__main__':
    print(min_window('ADOBECODEBANC', 'ABC'))