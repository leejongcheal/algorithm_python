# 경로의 갯수 + 확률 인데 깔끔하네 풀이가 와... 발상어떻게 한거지
# DP인건 알겠어 경로를 이런식으로 깔끔하게 구하네 절대  발상 못할듯
# 시간 초과뜸 따라서 재귀 안쓰고 풀수있는 방법으로 한번 풀어보자
import sys


def solve(day, climbed):
    global dic, m, n
    if day == m:
        if climbed >= n:
            return 1
        else:
            return 0
    if dic.get((day, climbed), -1) != -1:
        return dic[(day, climbed)]
    dic[(day,climbed)] = 0.25*solve(day+1,climbed+1) + 0.75*solve(day+1,climbed+2)
    return dic[(day,climbed)]


read = sys.stdin.readline
ans = []
for _ in range(int(read())):
    dic = dict()
    n, m = map(int, read().split())
    ans.append(solve(0, 0))
for a in ans:
    sys.stdout.write("%.10f\n"%(a))
