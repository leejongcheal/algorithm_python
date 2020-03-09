import sys
t = int(input())
name = sys.stdin.read().splitlines()
for idx in range(t):
    print(sorted([int(i) for i in name[idx].split()])[7])
