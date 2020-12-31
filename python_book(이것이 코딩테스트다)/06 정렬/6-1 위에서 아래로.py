n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))
L.sort(reverse=1)
for i in L:
    print(i, end=" ")