from collections import deque

def read_obstacles(filename):
    obstacles = []
    with open(filename, "r") as f:
        for line in f:
            n, e, s, w = map(int, line.split())
            
            x = e - w
            y = n - s
            
            obstacles.append((x, y))
    
    return obstacles


def create_grid(size, obstacles):
    grid = [[1 for _ in range(size)] for _ in range(size)]

    for x, y in obstacles:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = 0   # mark obstacle

    return grid
    
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def shortest_path(grid, start=(0,0), end=(10,10)):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    
    queue = deque()
    queue.append((start[0], start[1], 0))  # (x, y, distance)
    
    visited[start[1]][start[0]] = True

    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # N,E,S,W

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # no path
    
size = 20  # grid size

obstacles = read_obstacles("sample.txt")
grid = create_grid(size, obstacles)

print("Arena Map:")
print_grid(grid)

distance = shortest_path(grid)

print("\nShortest Path Distance:", distance)
