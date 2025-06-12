def isAnagram_dict(str1, str2):
    str1_dict = {}
    str2_dict = {}
    for letter in str1:
        if letter not in str1_dict:
            str1_dict[letter] = 1
        elif letter in str1_dict:
            str1_dict[letter] += 1

    for letter in str2:
        if letter not in str2_dict:
            str2_dict[letter] = 1
        elif letter in str2_dict:
            str2_dict[letter] += 1

    return False if len(str1_dict) != len(str2_dict) else True

if __name__ == '__main__':
    print(isAnagram_dict("abba", "abba"))