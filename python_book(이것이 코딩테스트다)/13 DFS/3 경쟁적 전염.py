"""
발상 완전탐색 n^2 * S * K 에서 몇천만 단위 넘음
virus 리스트를 사용해서 풀이 다돌면서 k인경우 + visit 사용해서 푸는건 N^2의 시간복잡도

완전탐색대신 virus 2차원 리스트를 사용해서 그거에 대해서만 검사후 전이를 시킴
-> 통과

위의 2차원 리스트 대신 heapq를 사용해서 푸는 방법도 있네 ㅋㅋ
핵심은 virus에 추가된 인덱스들은 나중에 추가해서 방문된곳을 또 방문해서 전이시키는 것을
안하는게 중요핵심임 -> visit을 하냐 이거야

"""
from collections import deque

steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())
virus = [[] for _ in range(K)]
blank = N * N
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            blank -= 1
            virus[Map[i][j] - 1].append((i, j))
X -= 1
Y -= 1
flag = 0
for time in range(S):
    # k+1 이 현재 바이러스번호 로 사용하기
    for k in range(K):
        temp = []
        while virus[k]:
            x, y = virus[k].pop()
            temp.append((x, y))
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == 0:
                    Map[nx][ny] = k+1
                    blank -= 1
                    temp.append((nx, ny))
            if blank == 0:
                flag = 1
                break
        virus[k] = temp
        if flag == 1:
            break
    if flag == 1:
        break
        virus[k] = temp

print(Map[X][Y])