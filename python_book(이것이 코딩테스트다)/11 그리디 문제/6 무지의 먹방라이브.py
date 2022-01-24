import heapq


def solution(food_times, k):
    N = len(food_times)
    if sum(food_times) <= k:
        return -1
    now_k = 0
    turn = 0
    q = []
    for i in range(N):
        heapq.heappush(q,(food_times[i], i))
    while k >= now_k + N*(q[0][0] - turn):
        value, index = heapq.heappop(q)
        if value <= turn:
            N -= 1
            continue
        now_k += N * (value - turn)
        turn = value
        N -= 1
    q.sort(key=lambda x : x[1])
    return q[(k - now_k)%N][1] + 1


L = list(map(int, input().split()))
k = int(input())
print(solution(L,k))




L = list(map(int, input().split()))
K = int(input())
print(solution(L,K))