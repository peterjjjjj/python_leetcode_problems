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

    def dfs(coordinates: tuple[int, int], target_char_index: int) -> bool:
        if target_char_index >= len(word):
            return True

        if not board[coordinates[0]][coordinates[1]] == word[target_char_index]:
            return False

        #check the char under
        if coordinates[0] < board_rows - 1:
            new_coordinates = (coordinates[0] + 1, coordinates[1])
            return dfs(new_coordinates, target_char_index + 1)

        #check the char above
        if coordinates[0] > 0:
            new_coordinates = (coordinates[0] - 1, coordinates[1])
            return dfs(new_coordinates, target_char_index + 1)

        #check the char at the right
        if coordinates[1] < board_cols - 1:
            new_coordinates = (coordinates[0], coordinates[1] + 1)
            return dfs(new_coordinates, target_char_index + 1)

        #check the char at the left
        if coordinates[1] > 0:
            new_coordinates = (coordinates[0], coordinates[1] - 1)
            return dfs(new_coordinates, target_char_index + 1)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                return dfs((i, j), 0)

if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['F', 'F', 'F', 'F'], ['G', 'G', 'G', 'G']]
    target_word = 'AFG'
    print(exist(board, target_word))