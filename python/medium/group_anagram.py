def group_anagrams(words):
    groups = {}
    for word in words:
        sorted_word = sorted(word)
        sorted_word = "".join(sorted_word)

        if sorted_word not in groups:
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)

    return list(groups.values())

if __name__ == '__main__':
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

