def longestSubstring(string):
    left = 0
    right = 0
    length = 0
    current_substring = []
    substrings = []
    substring_length = 0
    for i in range(len(string)):
        if string[i] not in current_substring:
            right = i
            current_substring.append(string[i])
            length += 1
            continue
        if length > substring_length:
            substrings = (string[left:right+1])
            left = i+1
            current_substring = []
            substring_length = length
            length = 0



    if length > substring_length:
        substrings = (string[left:right + 1])

    return substrings

if __name__ == '__main__':
    print(longestSubstring('abcdefgarjial'))