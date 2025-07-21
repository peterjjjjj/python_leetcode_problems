def water_flow(heights: list[list[int]]) -> list[list[int]]:
    """
    See Leetcode problem 417, basically find the cells that can reach either one of the top/left border or bottom/right border.
    If value of a cell is >= than neighbor, the neighbor cell is reachable.

    :param heights: list[list[int]]
    :return: list[list[int]]
    """

    if not heights:
        return []

    #Initialize 2 sets for the top/left and bottom/right borders.
    top_left = set()
    bottom_right = set()

    rows, cols = len(heights), len(heights[0])

    # Define directions for neighbors: (row_change, col_change)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

    def dfs(r: int, c: int, visited_set: set):
        # Add the current cell to the visited set (reachable from this ocean)
        visited_set.add((r, c))

        # Explore neighbors
        for row_direction, column_direction in directions:
            new_row, new_column = r + row_direction, c + column_direction # New row, new column

            # Check if the neighbor is in bounds
            if 0 <= new_row < rows and 0 <= new_column < cols:
                # Check if the neighbor hasn't been visited yet by this ocean's flow
                if (new_row, new_column) not in visited_set:
                    # Crucial: For reverse flow, water can move from lower/equal height to higher height
                    # So, the 'neighbor' cell (new_row, new_column) must be greater than or equal to the 'current' cell (r, c)
                    if heights[new_row][new_column] >= heights[r][c]:
                        dfs(new_row, new_column, visited_set)

    # Top row
    for c in range(cols):
        dfs(0, c, top_left)
    # Left column
    for r in range(rows):
        dfs(r, 0, top_left)

    # Bottom row
    for c in range(cols):
        dfs(rows - 1, c, bottom_right)
    # Right column
    for r in range(rows):
        dfs(r, cols - 1, bottom_right)

    result = []
    # The intersection of the two sets gives us the cells that can reach both oceans
    for r, c in top_left.intersection(bottom_right):
        result.append([r, c]) # Convert back to list for the output format

    return result



if __name__ == '__main__':
    print(water_flow([[1,2,2,3,5], [3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


