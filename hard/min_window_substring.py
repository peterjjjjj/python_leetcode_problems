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
    t_freq = dict()
    for char in t:
        if char not in t_freq:
            t_freq[char] = 1
        else:
            t_freq[char] += 1

    left = 0
    right = 0
    require_freq = t_freq
    for char in s[left:right]:
        if char in require_freq:
