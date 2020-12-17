import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
cnt = 0;
for i in range(a):
    for j in range(b):
        for x in range(c):
            print(i, j, x)
            cnt += 1
print(cnt)