import sys
N,M = map(int,input().split())
n = []
m = []
nameList = sys.stdin.read().splitlines()
n = nameList[:N]
m = nameList[N:]
result = set(n) & set(m)
result = list(result)
result.sort()
print(len(result))
for i in result:
    print(i)
