import heapq

def get_neighbors(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []

    if row > 0:
        neighbors.append(((row - 1, col), grid[row - 1][col]))
    if row < rows - 1:
        neighbors.append(((row + 1, col), grid[row + 1][col]))
    if col > 0:
        neighbors.append(((row, col - 1), grid[row][col - 1]))
    if col < cols - 1:
        neighbors.append(((row, col + 1), grid[row][col + 1]))

    return neighbors


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def append(self, key, value):
        heapq.heappush(self.pq, (value, key))

    def pop_lowest(self):
        value, key = heapq.heappop(self.pq)
        return key, value

    def __len__(self):
        return len(self.pq)

def dijkstra(grid, start, end):
    pq = PriorityQueue()
    visited = set()
    start_row, start_col = start
    end_row, end_col = end
    distances = [[float("inf") for _ in range(len(grid))] for _ in range(len(grid[0]))]
    distances[start_row][start_col] = 0
    pq.append(start, 0)

    while len(pq) > 0:
        #pop the item with the lowest value
        vertex, value = pq.pop_lowest()
        current_row, current_col = vertex

        if vertex in visited:
            continue
        visited.add((current_row, current_col))

        if vertex == end:
            return distances[end[0]][end[1]]

        for neighbor_position, neighbor_val in get_neighbors(grid, current_row, current_col):
            if neighbor_position not in visited:
                new_distance = value + neighbor_val
                neighbor_row, neighbor_col = neighbor_position
                if new_distance < distances[neighbor_row][neighbor_col]:
                    #distances[neighbor_row][neighbor_col] should be inf
                    distances[neighbor_row][neighbor_col] = new_distance
                    pq.append(neighbor_position, new_distance)

if __name__ == '__main__':
    #part 1 testcase
    grid = []
    with open('15_test.txt', 'r') as f:
        for line in f:
            row = [int(digit) for digit in line.strip()]
            grid.append(row)

    print(dijkstra(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1)))

    #part 1
    grid = []
    with open('15.txt', 'r') as f:
        for line in f:
            row = [int(digit) for digit in line.strip()]
            grid.append(row)

    print(dijkstra(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1)))

    #part 2 testcase
    grid = []
    with open('15_test_part2.txt', 'r') as f:
        for line in f:
            row = [int(digit) for digit in line.strip()]
            grid.append(row)

    print(dijkstra(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1)))

    #part 2
    grid = []
    with open('15.txt', 'r') as f:
        for line in f:
            row = [int(digit) for digit in line.strip()]
            grid.append(row)

    print(dijkstra(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1)))



