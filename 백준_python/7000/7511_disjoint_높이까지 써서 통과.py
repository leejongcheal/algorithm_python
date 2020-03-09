import sys


def Find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        p = Find(parent[x])
        parent[x] = p
        return p


# x < y 로 넣어주기
def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1


def is_join(x, y):
    global parent
    if Find(x) == Find(y):
        return 1
    else:
        return 0


input = sys.stdin.readline
t = int(input())
res = []
for idx in range(t):
    n = int(input())
    k = int(input())
    print("Scenario {}:".format(idx + 1))
    parent = [i for i in range(n)]
    rank = [0]*n
    for _ in range(k):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        Union(a, b)
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        if is_join(x, y) == 1:
            print("1")
        else:
            print("0")
    print(parent)
    print()
