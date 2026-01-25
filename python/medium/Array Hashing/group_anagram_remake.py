def sorting(strs: list[str]) -> list[list[str]]:
    combinations = dict()
    anagrams = []

    for word in strs:
        key = "".join(sorted(word.lower()))
        if key in combinations:
            combinations[key].append(word)
        else:
            combinations[key] = [word]

    for combination in combinations.values():
        anagrams.append(combination)

    return anagrams


def tuple_hash(strs: list[str]) -> list[list[str]]:
    hash_map = dict()
    anagrams = []

    for word in strs:
        # Empty letter char
        letters = [0 for _ in range(26)]

        for char in list(word.lower()):
            #Increment the corresponding letter count
            letters[ord(char) - ord('a')] += 1

        letter_tuple = tuple(letters)

        if letter_tuple in hash_map:
            hash_map[letter_tuple].append(word)

        else:
            hash_map[letter_tuple] = [word]


    for combination in hash_map.values():
        anagrams.append(combination)

    return anagrams

def tuple_hashing_practice(strs: list[str]) -> list[list[str]]:
    tuple_map = dict()
    anagrams = []

    for word in strs:
        letter_frequency = [0 for _ in range(26)]

        for char in list(word.lower()):
            letter_frequency[ord(char) - ord('a')] += 1

        letter_tuple = tuple(letter_frequency)

        if letter_tuple in tuple_map:
            tuple_map[letter_tuple].append(word)

        else:
            tuple_map[letter_tuple] = [word]

    for combination in tuple_map.values():
        anagrams.append(combination)

    return anagrams
if __name__ == '__main__':
    print(sorting(["eat","tea","tan","ate","nat","bat"]))
    print(tuple_hash(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(tuple_hashing_practice(["eat", "tea", "tan", "ate", "nat", "bat"]))

