from itertools import *
while True:
    n = input().split()[1:]
    if not n:
        break
    for c in combinations(n,6):
        print(" ".join(c))
    print()
