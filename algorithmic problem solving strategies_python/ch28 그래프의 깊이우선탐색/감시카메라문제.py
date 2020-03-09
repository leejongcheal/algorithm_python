import sys
sys.setrecursionlimit(10 ** 8)


# 오우 쉣 멋진문제
# 0 감시안됨
# 1 설치는 안했지만 감시됨
# 2 설치함
def dfs(here):
    global abj, visit, res, g, unwatched, watched, installed
    visit[here] = 1
    children = [0] * 3
    for there in range(g):
        if visit[there] == 0 and abj[here][there] == 1:
            children[dfs(there)] += 1
    if children[unwatched] > 0:  # 자식중 하나라도 감시안되는게 있으면 설치
        res += 1
        return installed
    elif children[installed] > 0:  # 설치된 자식 + 나머지 자식은 감시되고 있으면 자신도 감시되는중
        return watched
    else:  # 자식들이 모두 감시만 되는 경우 or 자식이 없는 경우 or 잎노드인경우
        return unwatched


def solve():
    global abj, visit, res, g, unwatched
    for i in range(g):
        if visit[i] == 0:
            if dfs(i) == unwatched:
                res += 1


unwatched = 0
watched = 1
installed = 2
T = int(input())
for _ in range(T):
    g, h = map(int, input().split())
    abj = []
    visit = [0] * g
    res = 0
    for i in range(g):
        abj.append([0] * g)
    for i in range(h):
        x, y = map(int, input().split())
        abj[x][y] = 1
        abj[y][x] = 1
    solve()
    print(res)
