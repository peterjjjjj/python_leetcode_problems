def num_islands_seperate(grid: list[list[str]]) -> int:
    r_limit = len(grid)
    c_limit = len(grid[0])
    num_islands = 0

    def mark_land(r: int, c: int):
        nonlocal grid
        #boundary check
        if r < 0 or r >= r_limit or c < 0 or c >= c_limit:
            return
        #check for land
        if grid[r][c] == '0' or grid[r][c] == '#':
            return

        #replace land
        grid[r][c] = '#'

        #up
        mark_land(r - 1, c)
        #down
        mark_land(r + 1, c)
        #left
        mark_land(r, c - 1)
        #right
        mark_land(r, c + 1)

    def dfs():
        nonlocal num_islands

        for i in range(r_limit):
            for j in range(c_limit):
                if grid[i][j] == '1':
                    num_islands += 1
                    mark_land(i, j)


    dfs()
    return num_islands


def num_islands_in1(grid: list[list[str]]) -> int:
    r_limit = len(grid)
    c_limit = len(grid[0])
    num_islands_count = 0

    def dfs(r: int, c: int):
        nonlocal num_islands_count

        #boundary check
        if r < 0 or r >= r_limit or c < 0 or c >= c_limit:
            return

        #check if sea or visited
        if grid[r][c] == '0' or grid[r][c] == '#':
            return

        #mark visited
        grid[r][c] = '#'

        #up
        dfs(r - 1, c)
        #down
        dfs(r + 1, c)
        #left
        dfs(r, c - 1)
        #right
        dfs(r, c + 1)

    for i in range(r_limit):
        for j in range(c_limit):
            if grid[i][j] == '1':
                num_islands_count += 1
                dfs(i, j)

    return num_islands_count



if __name__ == '__main__':
    test_grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print(num_islands_seperate(test_grid))
    test_grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print(num_islands_in1(test_grid))