"""
아오 문제좀 잘읽자 제발
상대적인 등수가 바뀐 쌍의 수 m 후에
1 2에 대해서 1과 2의 상대적 순위가 바뀐다는 뜻인데
1 -> 2 상황을 2 -> 1로 바꾼다는걸로 생각하고 풀어서 틀림 ㅋㅋ
알고리즘은 맞는데 문제를 잘못읽어서 틀리는 경우
"""
def solution(N, L, indegree):
    q = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            break
    res = []
    while q:
        if len(q) > 1:
            return "?"
        now = q.pop()
        res.append(now)
        for next in L[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    if len(res) != N:
        return "IMPOSSIBLE"
    elif len(res) == N:
        res.reverse()
        return " ".join(map(str, res))


T = int(input())
for tc in range(T):
    N = int(input())
    L = [[] for _ in range(N + 1)]
    score = list(map(int, input().split()))
    indegree = [0] * (N + 1)
    for i in range(N):
        b = score[i]
        for j in range(i+1, N):
            indegree[b] += 1
            a = score[j]
            L[a].append(b)
    M = int(input())
    for _ in range(M):
        a, b = map(int,input().split())
        temp = []
        if a in L[b]:
            a, b = b, a
        for la in L[a]:
            if la == b:
                continue
            temp.append(la)
        L[a] = temp
        L[b].append(a)
        indegree[b] -= 1
        indegree[a] += 1
    print(solution(N, L, indegree))