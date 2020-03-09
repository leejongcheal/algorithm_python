import sys
input = sys.stdin.readline
r = ""
for t in range(int(input())):
    n = int(input())
    a = [0]*n
    for i in range(n):
        x,y = map(int,input().split())
        a[x - 1] = y - 1
    result = 0
    min = n
    for i in range(n):
        if a[i] < min:
            min = a[i]
            result += 1
    r += str(result)+"\n"
print(r)
