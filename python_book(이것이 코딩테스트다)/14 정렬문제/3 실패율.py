def solution(N, stages):
    answer = []
    stages.sort()
    res = []
    Players = len(stages)
    for i in range(1,N+1):
        print(Players)
        cnt = stages.count(i)
        if cnt == 0 or Players == 0:
            res.append((i,0))
        else:
            res.append((i,cnt / Players))
            Players -= cnt
    print(res)
    res.sort(key=lambda x: x[1], reverse=True)
    for r in res:
        answer.append(r[0])
    return answer

N = int(input())
stages = list(map(int, input().split()))
print(solution(N, stages))