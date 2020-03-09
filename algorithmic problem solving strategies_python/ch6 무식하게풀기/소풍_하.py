# 재귀로 풀기로함 짝을 지어줄때 max,min으로 해서 넣어주면 순서가 강제 될줄 알았는데
# 01 23 45 // 01 45 23의 경우의수가 생김
# 이를 위해서 채울떄 x(firstx)을 pair에 없는수중 가장 작은수만 넣어서 푸는식으로 변경해서 pair의 순서를 강제한다.
# 0으로 먼저 시작만 하면 되는줄 알았는데 저생각은 왜 못했을까 ㅜㅜ
import sys


def CountPairing(pair):
    global n, ML, res
    if len(pair) == n:
        res += 1
        return
    firstx = n
    for x in range(n):
        if x not in pair:
            firstx = x
            break
    pair.append(firstx)
    for y in ML[firstx]:
        if y not in pair:
            pair.append(y)
            CountPairing(pair)
            pair.pop()
    pair.pop()


T = int(input())
read = sys.stdin.readline
for _ in range(T):
    n, m = map(int, read().split())
    L = list(map(int, read().split()))
    ML = []
    res = 0
    for _ in range(n):
        ML.append([])
    for i in range(m):
        a, b = min(L[2 * i], L[2 * i + 1]), max(L[2 * i], L[2 * i + 1])
        ML[a].append(b)
    CountPairing([])
    print(res)
