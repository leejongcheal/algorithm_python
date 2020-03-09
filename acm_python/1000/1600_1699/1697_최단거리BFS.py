from collections import deque

N, K = map(int, input().split())

if N > K:
    print(N - K)
    exit()
q = deque()
result = 0
dic = {}
q.append([N, result])
while q:
    d = q.popleft()
    if d[0] == K:
        print(d[1])
        exit()
    if dic.get(d[0] - 1, 0) == 0 and d[0] - 1 >= 0:
        dic[d[0] - 1] = 1
        q.append([d[0] - 1, d[1] + 1])
    if dic.get(d[0] + 1, 0) == 0 and d[0] + 1 <= 100000:
        dic[d[0] + 1] = 1
        q.append([d[0] + 1, d[1] + 1])
    if dic.get(2 * d[0], 0) == 0 and 2 * d[0] <= 100000:
        dic[2 * d[0]] = 1
        q.append([2 * d[0], d[1] + 1])
