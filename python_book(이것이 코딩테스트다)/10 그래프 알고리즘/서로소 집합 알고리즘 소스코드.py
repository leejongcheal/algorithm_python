# 루트 노드 찾는 함수
def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 루트노드 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 노드와 간선갯수 받음
v, e = map(int,input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

print(parent)
# 생략: 집합을 보고싶으면 위의 결과에대해서 루트값을 찾으면 됨