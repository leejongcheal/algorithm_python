import sys,time



R, C = map(int, input().split())
a = sys.stdin.read().splitlines()
c = time.time()
n = []
result = 0
for i in range(R):
    n.append(a[i])
print(n)
print(time.time() - c)