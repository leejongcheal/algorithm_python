import sys
L = sys.stdin.read().splitlines()
for idx in range(1,len(L)):
    a,b = L[idx].split()
    s = 0
    for c in a:
        if a.count(c) != b.count(c):
            print("{} & {} are NOT anagrams.".format(a,b))
            s = 1
            break
    if s == 0:
        print("{} & {} are anagrams.".format(a,b))
