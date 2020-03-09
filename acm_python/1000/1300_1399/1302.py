N = int(input())
dic = {}
for i in range(N):
    s = input()
    dic[s] = dic.get(s,0) + 1
max_v = 0
max_k = 0
for k,v in dic.items():
    if v > max_v:
        max_v = v
        max_k = k
    elif max_v == v:
        if max_k > k:
            max_k = k
print(max_k)
