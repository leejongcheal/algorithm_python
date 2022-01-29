from itertools import permutations
def solution(n, weak, dist):
    W = len(weak)
    D = len(dist)
    dist.sort(reverse=True)
    weak2 = []
    res = int(1e10)
    # 커버되는곳은 1로 두어서 나중에 연속1의 갯수가 W개 나오는지를 확인해서 다커버하는지 확인
    check_weak2 = [0]*2*n
    for i in range(len(weak)):
        weak2.append(weak[i])
    for i in range(len(weak)):
        weak2.append(n + weak[i])
    for dist_list in permutations(dist, D):
        for start_index in range(W):
            now = start_index
            flag = 0
            check_weak2 = [0]*W
            for i in range(len(dist_list)):
                start = weak2[now]
                end = weak2[now] + dist_list[i]
                for j in range(now, 2*W):
                    if start <= weak2[j] <= end:
                        check_weak2[j%W] = 1
                        if check_weak2.count(1) == W:
                            res = min(res, i + 1)
                            flag = 1
                    else:
                        now = j
                        break
                if flag == 1:
                    break
    if res < int(1e10):
        return res
    else:
        return -1

"""나는 weak에 대해서 인원을 1~D(W보다 작은값에 대해서) prem을 구한다음에
친구리스트는 그대로해서 넣어서 다 커버하는지 확인을 했는데 시간초과가 뜸

답지는 dist에 대해서 D의 갯수로 perm 한번 구한다음에 이걸로 시작점을 0~ W-1 시작으로 두어서
구한 dist_list로 다 채우는지확인해서 채우고나서 min cnt를 구하는 방식으로 푸니 시간이 훨씬 단축됨
--> 애매한 문제

통과는 했는데 내가 볼땐 check_weak2 부분에서 시간이 생각보다 오래걸리는듯?
-> 밑의 코드처럼 weak에 대해서 1~W순서로 perm 해서 푸니깐 어쩌피 시간초과임 perm자체를 줄이는 식으로
알고리즘을 짯어야함
"""

# from itertools import permutations
# def solution(n, weak, dist):
#     W = len(weak)
#     D = len(dist)
#     dist.sort(reverse=True)
#     weak2 = []
#     # 커버되는곳은 1로 두어서 나중에 연속1의 갯수가 W개 나오는지를 확인해서 다커버하는지 확인
#     check_weak2 = [0]*2*n
#     for i in range(len(weak)):
#         weak2.append(weak[i])
#     for i in range(len(weak)):
#         weak2.append(n + weak[i])
#     for cnt in range(1, D+1):#D + 1):
#         # W < D 인경우 1~W-1 까지 해서 못구했으면 W명 넣으면 무조건 커버하니 답
#         if cnt == W:
#             return cnt
#         for weak_list in permutations(weak, cnt):
#             # print(cnt, list(weak_list))
#             di = 0
#             check_weak2 = [0] * n
#             for w in list(weak_list):
#                 start = w
#                 end = w + dist[di]
#                 for i in range(2*W):
#                     if start <= weak2[i] <= end:
#                         check_weak2[i % W] = 1
#                         if check_weak2.count(1) == W:
#                             return cnt
#                 di += 1
#     return -1







n = int(input())
weak = list(map(int,input().split()))
dist = list(map(int, input().split()))
print(solution(n,weak,dist))