# 일단 완전 탐색이 왜 안되는지 부터 발상
# 최대 10000개의 숫자를 3~5개 조각들로 짤라야함 7개인 경우 2가지 경우가 나옴
# 7*1400이 만개정도이니 2^1400 아예 불가능 따라서 다른 방법 DP
# 3~5라는 유한 숫자가 주어짐 여기서 힌트얻어야함
# f = min(3,4,5(l) +f(l~n) )
# 메모리 제이션 발상을 못함 처음엔 3~6의 이런식으로 저장할려했는데 노쓸모라서
# 근데 S[begin]에서 이미 최솟값을 구했다면 그리고 3으로 먼저 싹돌고 4로 도는데 겹칠수가 있으니 메모리제이션!
# 시간초과 때문에 답지 참고함
# 3,4,5에 따른 계산 함수 만들고(이게 핵심인듯 ㅜ) 답도 ans 배열에 넣은다음에 바로 넣기 + dp를 굳이 재귀로? + 굳이 뒤에서부터? 앞에서 부터 풀어도 되자늠 ㅡㅡ
# 정말... 풀이 좆같은 책이였다 ㅅㅂ ㅋㅋㅋ 파이썬만 답 확인할수 있게 해주면 개좋을텐데
import sys


def score_3(a, b, c):
    if a == b == c:
        return 1
    elif b - a == c - b == 1 or b - a == c - b == -1:
        return 2
    elif a == c != b:
        return 4
    elif b - a == c - b:
        return 5
    else:
        return 10


def score_4(a, b, c, d):
    if a == b == c == d:
        return 1
    elif b - a == c - b == d - c:
        if b - a == 1 or b - a == -1:
            return 2
        else:
            return 5
    elif a == c and b == d and a != b:
        return 4
    else:
        return 10


def score_5(a, b, c, d, e):
    if a == b == c == d == e:
        return 1
    elif b - a == c - b == d - c == e - d:
        if b - a == 1 or b - a == -1:
            return 2
        else:
            return 5
    elif a == c == e and b == d and a != b:
        return 4
    else:
        return 10


def solve(arr):
    n = len(arr)
    res = [-1] * (n + 1)
    res[3] = score_3(arr[0], arr[1], arr[2])
    res[4] = score_4(arr[0], arr[1], arr[2], arr[3])
    res[5] = score_5(arr[0], arr[1], arr[2], arr[3], arr[4])
    for i in range(6, n + 1):
        r = sys.maxsize
        if res[i - 3] != -1:
            r = min(r, res[i - 3] + score_3(arr[i - 3], arr[i - 2], arr[i - 1]))
        if res[i - 4] != -1:
            r = min(r, res[i - 4] + score_4(arr[i - 4], arr[i - 3], arr[i - 2], arr[i - 1]))
        if res[i - 5] != -1:
            r = min(r, res[i - 5] + score_5(arr[i - 5], arr[i - 4], arr[i - 3], arr[i - 2], arr[i - 1]))
        res[i] = r
    return res[-1]


read = sys.stdin.readline
ans = []
T = int(read())
for _ in range(T):
    line = read().strip()
    L = list(map(int, line))
    ans.append(solve(L))
for c in ans:
    sys.stdout.write("{}\n".format(c))
