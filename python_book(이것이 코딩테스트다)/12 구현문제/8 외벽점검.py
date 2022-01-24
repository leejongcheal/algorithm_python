from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    answer = n + 1
    for i in range(length):
        weak.append(weak[i] + n)
    for start_index in range(length):
        for friends in list(permutations(dist,len(dist))):
            cnt = 1
            # 처음 친구의 최대위치
            position = weak[start_index] + friends[cnt - 1]
            # 어디 까지 가는지 검사
            for i in range(start_index, start_index + length):
                # 더갈수 있음
                if position >= weak[i]:
                    continue
                # 못간곳에서 친구 떨어질떄까지 더해서 가능한지 보기
                else:
                    cnt += 1
                    if cnt > len(friends):
                        break
                    position = weak[i] + friends[cnt - 1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    else:
        return answer



n = int(input())
weak = list(map(int,input().split()))
dist = list(map(int, input().split()))
print(solution(n,weak,dist))