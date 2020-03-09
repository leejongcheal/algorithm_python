def make_graph():
    global L, al, n
    for j in range(1, n):
        i = j - 1
        minlen = min(len(L[i]), len(L[j]))
        for k in range(minlen):
            if L[i][k] != L[j][k]:
                a = ord(L[i][k]) - ord('a')
                b = ord(L[j][k]) - ord('a')
                al[a][b] = 1
                break


def topologcalSort():
    global visit, al, order
    # 위상 그래프는 순서상관없이 dfs돌리면 알아서 순서 맞춰줌
    # ab, bc의 위상일떄 ac에 대해선 알아서 되니 걱정 노노(이런거 생각하면 불가능한 문제)
    for i in range(26):
        if visit[i] == 0:
            dfs(i)
    # 위배되는 순서있는지 확인
    for i in range(26):
        for j in range(i + 1, 26):
            if al[order[i]][order[j]] == 1:
                return 0
    return 1


def dfs(here):
    global visit, al, order
    visit[here] = 1
    for i in range(26):
        if visit[i] == 0 and al[here][i] == 1:
            dfs(i)
    order.append(here)


T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    al = []
    visit = [0] * 26
    order = []
    for _ in range(n):
        L.append(input())
    for i in range(26):
        al.append([0] * 26)
    make_graph()
    if topologcalSort() == 0:
        print("impossible")
    else:
        for c in order[::-1]:
            print("%c" % (chr(ord('a') + c)), end="")
        print()
