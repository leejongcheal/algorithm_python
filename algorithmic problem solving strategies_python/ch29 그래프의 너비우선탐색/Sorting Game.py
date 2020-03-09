# 개선한것
# [1] 1000 2000 3000 이나 1 2 3 이나 같다 0~ n-1번호로 다시 분배해준다.
# [2] 위의 바탕으로 입력 받은 n 에 대한 모든경우에 대해 미리 계산해 저장해둔다 .
from collections import deque


def precal(n):
    global toSort
    L = []
    for i in range(n):
        L.append(i)
    q = deque()
    q.append(L)
    toSort[tuple(L)] = 0
    while q:
        here = q.popleft()
        cnt = toSort[tuple(here)]
        for i in range(n-1):
            for j in range(i+1,n):
                there = here[0:i] + here[i:j+1][::-1] + here[j+1:]
                if toSort.get(tuple(there),-1) == -1:
                    toSort[tuple(there)] = cnt + 1
                    q.append(there)


T = int(input())
toSort = dict()
visit = [0]*10
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    if visit[n] == 0:
        visit[n] = 1
        precal(n)
    sortL = sorted(L)
    fixed = [0]*n
    for i in range(n):
        fixed[i] = sortL.index(L[i])
    print(toSort[tuple(fixed)])
