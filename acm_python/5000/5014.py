from collections import deque
high, start, des, up, down = map(int, input().split())
v = [0]*(high+1)
q = deque()
q.append(start)
v[start] = 1
while q:
    x = q.popleft()
    if x == des:
        print(v[x]-1)
        exit()
    if x+up <= high and v[x+up] == 0:
        v[x+up] = v[x] + 1
        q.append(x+up)
    if x-down > 0 and v[x-down] == 0:
        v[x-down] = v[x] + 1
        q.append(x-down)
print("use the stairs")
