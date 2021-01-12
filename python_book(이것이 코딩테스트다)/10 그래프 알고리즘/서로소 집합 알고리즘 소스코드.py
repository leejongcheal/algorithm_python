# 루트 노드 찾는 함수
def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 루트노드 찾기
    A = find_parent(parent, a)
    B = find_parent(parent, b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B
    # *** 처음 union 과정의 a,b가 아닌 서로의 루트인 A, B에 대해서 값 바꾸는것을 주의
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