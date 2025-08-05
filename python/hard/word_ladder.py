import collections


def word_ladder_bfs(start: str, end: str, word_list: list[str]) -> int:
    """
    Given two words, beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence from beginWord to endWord or 0 if no such sequence exists.


    :param start: int
    :param end: int
    :param word_list: list[int]
    :return: int
    """

    word_set = set(word_list)

    #Queue for the words to process.
    queue = collections.deque([(start, 1)])
    #Visited words.
    visited_list = set()

    visited_list.add(start)

    steps = 0

    while queue:
        current_word, steps = queue.popleft()

        if current_word == end:
            return steps

        for i in range(len(str(current_word))):
            #Use ASCII to generate 26 letters to find all combinations of possible words.
            original_word = current_word[:]
            current_word = list(current_word)


            for j in range(26):
                # To process the word, convert to list.
                current_word = list(current_word)

                #Replace the index with 26 letters.
                current_word[i] = chr(ord('a') + j)
                #Convert back to str.
                current_word = ''.join(current_word)

                if current_word not in visited_list:
                    if current_word in word_list:
                        if current_word == end:
                            return steps
                        queue.append((current_word, steps + 1))
                        visited_list.add(current_word)

            current_word = original_word[:]

    return 0


if __name__ == '__main__':
    print(word_ladder_bfs(start='hit', end='cog', word_list=["hot","dot","dog","lot","log","cog"]))



