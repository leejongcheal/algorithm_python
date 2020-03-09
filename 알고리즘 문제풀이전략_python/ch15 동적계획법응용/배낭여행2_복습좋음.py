# 이건 재귀함수의 진행과정을 정확히 이해 하고있을때 가능한 코딩방법
# cnt visit같은 경우는 들어올때 나갈때 꼭 숙지
# 재귀는 역시 탈출조건과 순서 중요
def traverse(src):
    global visit, fare, final_fare, cnt, n, L, res
    visit[src] = 1
    cnt += 1
    if cnt == n and L[src][0] != 0:
        res.append(fare + L[src][0])
        if final_fare > fare + L[src][0]:
            final_fare = fare + L[src][0]
            cnt -= 1
            visit[src] = 0
            return
    for i in range(n):
        if L[src][i] != 0 and visit[i] != 1:
            if final_fare < fare + L[src][i]:
                continue
            fare = fare + L[src][i]
            traverse(i)
            fare = fare - L[src][i]
    visit[src] = 0
    cnt -= 1

T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    visit = [0]*n
    fare = 0
    final_fare = 9999
    cnt = 0
    res = []
    traverse(0)
    # print(res)
    print(final_fare)
