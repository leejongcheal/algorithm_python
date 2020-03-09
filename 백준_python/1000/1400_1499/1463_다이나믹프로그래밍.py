dic = {1: 0, 0: 0, 2: 1, 3: 1}

N = int(input())
i = 0
for i in range(4, N + 1):
    if i % 3 == 0 and i % 2 == 0:
        dic[i] = min(dic[i // 3], dic[i // 2], dic[i - 1]) + 1
    elif i % 3 == 0:
        dic[i] = min(dic[i // 3], dic[i - 1]) + 1
    elif i % 2 == 0:
        dic[i] = min(dic[i // 2], dic[i - 1]) + 1
    else:
        dic[i] = dic[i-1] + 1
print(dic[N])
