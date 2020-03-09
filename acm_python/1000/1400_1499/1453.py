N = int(input())
X = list(map(int,input().split()))
dic = {}
res = 0
for i in X:
    if dic.get(i,0) == 0:
        dic[i] = 1
    else:
        res += 1
print(res)
