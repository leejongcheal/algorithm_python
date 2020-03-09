def disjoint(a, b):
    return a[1] <= b[0] or a[0] >= b[1]


def make_graph(meeting):
    global abj, n
    for i in range(2 * n):
        abj.append([])
    for i in range(0,n,2):
        j = i + 1
        abj[i * 2 + 1].append(j * 2)  # i~ -> j
        abj[j * 2 + 1].append(i * 2)  # j~ -> i
    for i in range(n):
        for j in range(i - 1):
            if disjoint(meeting[i], meeting[j]) == 0:
                abj[2 * i].append(j * 2 + 1)  # i -> ~j
                abj[2 * j].append(i * 2 + 1)


def scc(here):
    global n, sccld,discovered,finish,scccnt,vertexcnt,st,abj
    ret = discovered[here] = vertexcnt + 1
    vertexcnt += 1
    st.append(here)  # here의 자손들이 위로 계속 들어감

    for i in range(len(abj[here])):
        there = abj[here][i]
        # here there 가 트리간선 인지
        if discovered[there] == -1:
            ret = min(ret,scc(there))
        # 교차 간선인 경우 무시
        elif discovered[there] < discovered[here] and finish[there] != -1:
            ret = min(ret, discovered[there])
    #  here이 강결합 컴포넌트의 루트인지 확인한다.
    if ret == discovered[here]:
        while 1:
            if st:
                t = st.pop()
                #print(t,sccld)
                sccld[t] = scccnt
                if t == here:
                    break
        scccnt += 1
    finish[here] = 1
    return ret


def solve():
    global n, sccld,discovered,finish,scccnt,vertexcnt
    for i in range(2*n):
        if discovered[i] == -1:
            scc(i)
    for i in range(0,2*n,2):
        if sccld[i] == sccld[i+1]:
            return []# 문제풀이 불가능
    order = []
    value =[-1]*(2*n)
    for i in range(2*n):
        order.append([sccld[i], i])
    order.sort()
    for i in range(2*n):
        vertex = order[i][1]
        var = vertex//2
        isTrue = vertex%2
        if value[var] != -1:
            continue
        value[var] = 1-isTrue
    return value


T = int(input())
for _ in range(T):
    n = int(input())
    st = []
    meeting = []
    abj = []
    res = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        meeting.append([x1, y1])
        meeting.append([x2, y2])
    n = 2*n
    make_graph(meeting)
    sccld = [-1]*(2*n)
    discovered = [-1]*(2*n)
    finish = [-1]*(2*n)
    scccnt = 0
    vertexcnt = 0
    value = solve()
    if value == []:
        print("Impossible")
    else:
        for i in range(0,n,2):
            if value[i] == 1:
                print(meeting[i][0],meeting[i][1])
            else:
                print(meeting[i+1][0],meeting[i+1][1])
