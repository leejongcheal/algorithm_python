import sys
n,h = map(int,input().split())
name = sys.stdin.read().splitlines()
low = [0]*(h+2)
high = [0]*(h+2)
rl= [0]*(h+2)
rh = [0]*(h+2)
for idx in range(0,n,2):
    low[int(name[idx])] += 1
    high[int(name[idx+1])] += 1
for i in range(1,h+1):
    rl[h+1-i] = rl[h+2-i] + low[h+1-i]
    rh[i] = rh[i-1] + high[h+1-i]
total = []
for i in range(1,h+1):
    total.append(rl[i]+rh[i])
print(min(total),total.count(min(total)))
