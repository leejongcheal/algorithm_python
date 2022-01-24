def solution(N, M, graph):
    visit = [0]*N
    recursive(graph, visit)


def recursive(graph, visit):
    global N, result
    if sum(visit) == N:
        result += 1
        return
    for i in range(N):
        if visit[i] == 0:
            now = i
            break
    visit[now] = 1
    for next in graph[now]:
        if visit[next] == 0:
            visit[next] = 1
            recursive(graph, visit)
            visit[next] = 0
    visit[now] = 0


for test_case in range(int(input())):
    result = 0
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    word = list(map(int, input().split()))
    for i in range(M):
        x, y = word[i*2], word[i*2+1]
        graph[min(x, y)].append(max(x, y))
    solution(N, M, graph)
    print(result)