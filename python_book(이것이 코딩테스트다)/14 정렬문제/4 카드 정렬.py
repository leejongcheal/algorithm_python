import heapq
N = int(input())
L = []
for _ in range(N):
    heapq.heappush(L,int(input()))
res = 0
while len(L) >= 2:
    a = heapq.heappop(L)
    b = heapq.heappop(L)
    res += a + b
    heapq.heappush(L,a+b)
print(res)
"""
문제 이해에서 틀렸음 a + b 한걸 다시 L에 들어가서 sort 가 필요함
 -> 위에서 바로 heapq -> 정렬을 유지해야하는 리스트에 값을 계속 집어넣고 뺴야하는 경우에

"""