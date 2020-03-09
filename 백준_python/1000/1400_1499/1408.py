cur = list(map(int,input().split(":")))
start = list(map(int,input().split(":")))
result = [0,0,0]
for i in range(2,-1,-1):
    result[i] = start[i] - cur[i]
    if i != 0 and result[i] < 0:
        result[i] += 60
        start[i - 1] -= 1
    if i == 0 and result[i] < 0:
        result[i] += 24
print("%02d:%02d:%02d"%(result[0],result[1],result[2]))
