def exist(board: list[list[str]],
          word: str) -> bool:
    """
    Returns true if word exists in board, the word must be constructed by adjacent characters.

    :param board: m x n grid of letters
    :param word: string
    :return: boolean
    """
    board_rows = len(board)
    board_cols = len(board[0])
    word_len = len(word)

    def dfs(r: int, c: int, target_char_index: int) -> bool:
        #if have found all target chars
        if target_char_index >= word_len:
            return True

        #if row_index and column_index are out of range
        if not (0 <= r < board_rows and 0 <= c < board_cols):
            return False

        #if current char doesn't match
        if board[r][c] != word[target_char_index]:
            return False

        original_char = board[r][c]
        #mark the visited char
        board[r][c] = '!'

        result = (
            dfs(r + 1, c, target_char_index + 1) or
            dfs(r - 1, c, target_char_index + 1) or
            dfs(r, c + 1, target_char_index + 1) or
            dfs(r, c - 1, target_char_index + 1)
        )

        board[r][c] = original_char

        return result

    for i in range(board_rows):
        for j in range(board_cols):
            if board[i][j] == word[0]:
                if dfs(i, j, 0):
                    return True

    return False


if __name__ == '__main__':
    board1 = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    target_word = 'ABCCED'
    print(exist(board1, target_word))