
def word_ladder(start: str, end: str, word_list: list[str]) -> int:
    """
    Given two words, beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence from beginWord to endWord or 0 if no such sequence exists.


    :param start: int
    :param end: int
    :param word_list: list[int]
    :return: int
    """

    min_steps = 0
    visited_words = set()
    current_word = list(start)
    hash_table = dict()
    travel_list = list()

    def search_next(word: list[str]) -> int:
        nonlocal hash_table, min_steps

        min_steps += 1

        for i in range(len(start)):
            for j in range(26):
                new_word = word[:]
                new_word[i] = chr(ord('a') + j)
                result = ''.join(new_word)

                if result == end:
                    return min_steps

                if result in word_list:
                    key = word[:i] + word[i + 1:]
                    key = ''.join(key)
                    if not key in hash_table:
                        hash_table[key] = result
                        visited_words.add(result)
                        travel_list.append(result)

        next_word = travel_list.pop(0)
        next_word = list(next_word)
        search_next(next_word)

        return 0

    for _ in range(len(word_list)):
        search_next(current_word)

    return min_steps

if __name__ == '__main__':
    print(word_ladder(start='hit', end='cog', word_list=["hot","dot","dog","lot","log","cog"]))



