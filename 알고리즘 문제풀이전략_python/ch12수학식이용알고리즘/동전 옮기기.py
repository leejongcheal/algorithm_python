from collections import deque


def solve(L):
    n = len(L)
    sum = 0
    for x in L:
        sum += x
    mid = sum//n
    res = 0
    for x in L:
        res += abs(mid - x)
    print(res//2)

T = int(input())
q = deque()
for _ in range(T):
    n = int(input())
    L = []
    for _ in range(n):
        L.append(int(input()))
    q.append(L)

while q:
    solve(q.popleft())
