from sys import stdin
input = stdin.readline
n = int(input())
inter = []
for i in range(1, n+1):
    s, t = map(int,input().split())
    inter.append((s,1))
    inter.append((t,-1))
    #위처럼 쓰면 시작이랑 끝이 같은경우 끝이 앞으로 오는 효과 있음 와...
inter.sort()

maxroom = 0
curroom = 0
for t, ttype in inter:
    curroom+= ttype
    maxroom = max(maxroom, curroom)
print(maxroom)