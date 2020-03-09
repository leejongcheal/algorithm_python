# 오일러 문제로 풀기
# 끝말 있기는 오일러서킷 또는 오일러트레일로 문제풀이

# 오일러 서킷 또는 트레일인지 확인하기
def checkEuler():
    global indegree, outdegree
    plus1 = minus1 = 0
    for i in range(26):
        delta = outdegree[i] - indegree[i]
        if delta != 0 and delta != 1 and delta != -1:
            return -1
        elif delta == 1:
            plus1 += 1
        elif delta == -1:
            minus1 += 1
    # 트레일 또는 서킷일때 1반환
    if (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0):
        return 1


# 트레일 조건있으면 트레일 찾고 아니면 서킷 탐색
def getEulerTrailorCircuit():
    global L, res, n, abj,indegree, outdegree, res
    # 우선 트레일을 찾아본다
    for i in range(26):
        if outdegree[i] == indegree[i] + 1:
            getEuler(i)
            return
    # 아니면 서킷이나 간선에 인접한 아무 정점에서 시작
    for i in range(26):
        if(outdegree[i]):
            getEuler(i)
            return
    # 모두 실패한 경우
    return


def getEuler(here):
    global L, res, n, abj,indegree, outdegree, res
    for there in range(26):
        while abj[here][there]:
            abj[here][there] -= 1
            getEuler(there)
    res.append(here)
    # 함수가 끝날떄 넣어주니 거꾸로 해야 순서완성


# 그래프 만들기
def make_graph():
    global L, abj, n, Labj, indegree, outdegree
    for i in range(26):
        abj.append([0]*26)
        Labj.append([])
        for j in range(26):
            Labj[i].append([])
    for _ in range(n):
        L.append(input())
    for c in L:
        x = ord(c[0]) - ord('a')
        y = ord(c[-1]) - ord('a')
        abj[x][y] += 1
        outdegree[x] += 1
        indegree[y] += 1
        Labj[x][y].append(c)


T = int(input())
for _ in range(T):
    flag = 0
    n = int(input())
    L = []
    abj = []
    Labj = []
    indegree = [0]*26
    outdegree = [0]*26
    make_graph()
    res = []
    if checkEuler() == -1:
        print("Impossible")
    else:
        getEulerTrailorCircuit()
        if len(res) != (n+1):
            print("impossible")
        else:
            res = res[::-1]
            for i in range(n):
                print(Labj[res[i]][res[i+1]].pop())



