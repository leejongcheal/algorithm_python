from _collections import deque

n, m = map(int, input().split())
L = []
for _ in range(n):
    L.append(list(map(int, input())))
visited = [[0] * m for _ in range(n)]
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        break
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        # 갈수 있을때
        if 0 <= nx < n and 0 <= ny < m and L[nx][ny] != 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            L[nx][ny] = L[x][y] + 1
            queue.append((nx, ny))
print(L[n - 1][m - 1])
