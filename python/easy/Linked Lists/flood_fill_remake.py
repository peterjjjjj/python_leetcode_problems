def flood_fill_recursion(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if not image:
        return []

    if image[sr][sc] == color:
        return image

    def search(r: int, c: int, start_color: int) -> None:
        nonlocal image

        #Check for different num than intend, 2 cases: the nums that were changed already, different nums
        if image[r][c] != start_color:
            return

        #Change the current num to color
        image[r][c] = color

        # Up
        if r > 0:
            search(r - 1, c, start_color)
        # Down
        if r < len(image) - 1:
            search(r + 1, c, start_color)
        # Left
        if c > 0:
            search(r, c - 1, start_color)
        # Right
        if c < len(image[0]) - 1:
            search(r, c + 1, start_color)

    search(sr, sc, image[sr][sc])
    return image


if __name__ == "__main__":
    #print(flood_fill_recursion([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    print(flood_fill_recursion([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 0, 2))