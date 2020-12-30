from _collections import deque

n, m = map(int, input().split())
L = []
#visited 안쓰고 L에 표시해도 상관없음
# 상하좌우 배열
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0
for _ in range(n):
    L.append(list(map(int, input())))
for i in range(n):
    for j in range(m):
        if L[i][j] == 0:
            # bfs 실행
            queue = deque()
            L[i][j] = 1
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for step in steps:
                    nx = x + step[0]
                    ny = y + step[1]
                    # 인접하고 방문한적 없는 경우
                    if 0 <= nx < n and 0 <= ny < m and L[nx][ny] == 0:  # and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        L[nx][ny] = 1
            result += 1
print(result)
