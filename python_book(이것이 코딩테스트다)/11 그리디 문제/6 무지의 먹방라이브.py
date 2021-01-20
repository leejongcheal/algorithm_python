def solution(food_times, k):
    answer = 0
    n = len(food_times)
    N = n
    k += 1
    while 1:
        # k는 남아 있느데 n=0 이면 돌리 못하니 -1반환
        if n == 0:
            if k > 0:
                return -1
            # n= 0 k= 0 마지막값이 답인경우 끝까지 도는경우
            else:
                return last_index + 1
                break
        # 나머지값만 남아서 자리 찾으면 됨
        q = k // n
        r = k % n
        # print(k,n,q,r)
        if q <= 0:
            if k == 0:
                return last_index + 1
            break
        last_index = 0
        for i in range(N):
            # 돈 경우
            if food_times[i] != 0:
                # 몫의 횟수만큼 충분히 도는경우
                if food_times[i] > q:
                    food_times[i] -= q
                # 부분만 도는경우 남은수를 r에 더해줌
                else:
                    r += q - food_times[i]
                    n -= 1
                    food_times[i] = 0
                last_index = i
            # 아예 돌지않는경우 last_index무시
            else:
                pass
        # print(food_times)
        k = r
    for i in range(N):
        if food_times[i] != 0:
            k -= 1
            if k <= 0:
                return (i+1)




L = list(map(int, input().split()))
K = int(input())
print(solution(L,K))