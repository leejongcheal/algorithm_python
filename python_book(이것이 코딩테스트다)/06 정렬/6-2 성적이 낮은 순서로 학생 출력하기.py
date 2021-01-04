n = int(input())
dict = {}
for _ in range(n):
    a, b = input().split()
    dict[int(b)] = a
L = sorted(dict.keys())
for i in L:
    print(dict[i], end = ' ')