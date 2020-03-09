from collections import deque


def bfs(start):
    n = len(start)
    dic = dict()
    q = deque()
    result = sorted(start)
    q.append(start)
    dic[tuple(start)] = 0
    while q:
        here = q.popleft()
        cnt = dic[tuple(here)]
        if here == result:
            return cnt
        for i in range(n - 1):
            for j in range(i + 1, n):
                there = here[0:i] + here[i:j + 1][::-1] + here[j + 1:n]
                if dic.get(tuple(there), 0) == 0:
                    dic[tuple(there)] = cnt + 1
                    q.append(there)


T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    res = bfs(L)
    print(res)
