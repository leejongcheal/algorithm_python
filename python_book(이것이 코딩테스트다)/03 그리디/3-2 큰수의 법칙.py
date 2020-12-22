n, m, k = map(int,input().split())
L = list(map(int,input().split()))
f = max(L)
L.remove(f)
s = max(L)
flag = 0
result = 0
for i in range(m):
    flag += 1
    if flag >= k:
        result += s
        flag = 0
    else:
        result += f
print(result)
