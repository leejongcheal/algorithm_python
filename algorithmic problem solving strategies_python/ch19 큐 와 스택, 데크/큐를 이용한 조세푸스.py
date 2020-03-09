from collections import deque
T = int(input())
for _ in range(T):
    q = deque()
    n, k = map(int, input().split())
    for i in range(1,n+1):
        q.append(i)
    q.popleft()
    while len(q) != 2:
        i = 0
        while i<k-1:
            i += 1
            q.append(q.popleft())
        q.popleft()
    print(q.popleft(), q.popleft())
