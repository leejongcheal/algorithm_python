# 응 시간초과 아이디어는 좋은거 같은뎁..
# n에 맞춰 신호리스트를 계산하고 q에 하나하나 넣으면서 sum보다 크면 작아질때까지 pop한다음 넣어주는식으로 계산함
# 오프라인 알고리즘이 아닌 온라인 알고리즘으로 풀이
# 굳이 큐 안쓰고 배열에서 head, tail 가지고 노는게 더 빠른가? -> 파이썬으로 푼사람 아예없음
from collections import deque


def calSignal():
    global L, A, n, maxn, mod
    for i in range(maxn+1, n + 1):
        A.append(L[i - 1] % 10000 + 1)
        L.append(((L[-1] * 214013 + 2531011) % mod))
    maxn = n


T = int(input())
mod = 2 ** 32
maxn = 0 #5000000
L = [1983]
A = []
for _ in range(T):
    k, n = map(int, input().split())
    if n > maxn:
        calSignal()
    sum = 0
    res = 0
    q = deque()
    for i in range(n):
        q.append(A[i])
        sum += A[i]
        if sum > k:
            while sum > k:
                sum -= q.popleft()
        if sum == k:
            res += 1
    print(res)
