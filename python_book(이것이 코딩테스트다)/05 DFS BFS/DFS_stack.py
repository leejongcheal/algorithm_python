def bfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        # 1번 후순위 인접노드가 dfs중에 다른 노드의 인접노드로 겹치는 경우 방지
        if node not in visit:
            visit.append(node)
            # 인접 노드에서 우선순위가 앞의 노드에 있을경우
            # 사실 순서 상관없으면 reverse없이 사용해도 됨.
            stack.extend(graph[node].reverse())
    return visit