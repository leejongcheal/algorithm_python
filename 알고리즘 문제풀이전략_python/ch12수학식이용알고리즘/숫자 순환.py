def find_number(n,p):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c) ** p
    return sum


def solve(P):
    n = P[0]
    L = [n]
    while True:
        n = find_number(n, P[1])
        if n in L:
            print(L.index(n))

            return
        else:
            L.append(n)


T = int(input())
L = []
for _ in range(T):
    L.append(list(map(int, input().split())))
for x in L:
    solve(x)
