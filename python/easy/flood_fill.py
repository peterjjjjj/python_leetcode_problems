def flood_fill(image: list[list[int]], sr: int, sc: int, colour: int) -> list[list[int]]:
    """
    O(n)
    O(n)
    :param image:
    :param sr:
    :param sc:
    :param colour:
    :return:
    """
    r_range = len(image)
    c_range = len(image[0])
    start_colour = image[sr][sc]

    if start_colour == colour:
        return image

    def dfs(r: int, c: int,) -> None:
        nonlocal image, colour


        #boundary check
        if r < 0 or r >= r_range or c < 0 or c >= c_range:
            return

        #if current pixel has same num as starting pixel
        if image[r][c] == start_colour:
            #colour it
            image[r][c] = colour
        else:
            return

        #up
        dfs(r - 1, c)
        #down
        dfs(r + 1, c)
        #left
        dfs(r, c - 1)
        #right
        dfs(r, c + 1)


    dfs(sr, sc)
    return image

if __name__ == '__main__':
    image = [[0,0,0],[0,0,0]]
    print(flood_fill(image, sr=0, sc=0, colour=0))
