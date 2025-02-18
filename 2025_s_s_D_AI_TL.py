from collections import deque


def max_square(n, m, d, grid):
    distance = [[float('inf')] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'x':
                distance[i][j] = 0
                queue.append((i, j))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == float('inf'):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    max_square_size = 0
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'o' and distance[i][j] >= d:
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_square_size = max(max_square_size, dp[i][j])
    return max_square_size


n, m, d = map(int, input().split())
grid = [input().strip() for _ in range(n)]

result = max_square(n, m, d, grid)
print(result)
