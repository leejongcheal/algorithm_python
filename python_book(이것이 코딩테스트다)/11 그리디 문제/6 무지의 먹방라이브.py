import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(1, len(food_times)+1):
        heapq.heappush(q,(food_times[i-1], i))
    value = len(food_times)
    time = 0
    turn = 0
    while k >= time + (q[0][0]-turn)*value:
        min_turn, index = heapq.heappop(q)
        time += (min_turn - turn)*value
        turn = min_turn
        value -= 1
    q.sort(key=lambda x:x[1])
    return q[(k - time)%value][1]


L = list(map(int, input().split()))
k = int(input())
print(solution(L,k))




L = list(map(int, input().split()))
K = int(input())
print(solution(L,K))