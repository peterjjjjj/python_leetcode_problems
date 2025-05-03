def longestSubstring(string):
    left_index = 0
    char_set = set()
    max_length = 0
    result_start_index = 0

    for right_index in range(len(string)):
        current_char = string[right_index]

        #remove all items before index
        while current_char in char_set:
            char_set.remove(string[left_index])
            left_index += 1

        char_set.add(current_char)

        current_max_length = right_index + 1 - left_index
        if current_max_length > max_length:
            max_length = current_max_length
            result_start_index = left_index

    return string[result_start_index : result_start_index + max_length]


if __name__ == '__main__':
    print(longestSubstring('dvdfe'))
