"""
001, 010, 100 같은것은 list(map(int, input().split()))로 받으면
[1], [10], [100]의 값을 가진다. 띄어 쓰기가 없는경우에는 input().split()에 대해서 list화 하기보다는
input()자체에 list화 를 한다. 위의 경우 list(map(int, input()))을 사용한다.
input()자체에 리스트화를 하면 한글자 한글자 원소화 시켜서 값을 저장한다.
ex) asd -> ['a', 's', 'd'] // a s d -> ['a', ' ', 's', ' ', 'd']
"""
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
