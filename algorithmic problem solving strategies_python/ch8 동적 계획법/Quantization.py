# 정렬후 s개의 묶음으로 묶은후에 그들의 평균값(반올림)으로 양자화값  구함<핵심발상>
# s개로 묶는다 -> 유한 DP 어떤식으로 묶을건지 문제 추상화!!
# 결과 (A-m)^2 = A^2 + 2mA + m^2 인걸 이용하기위해 psum , ppsum을 미리 계산해서 시간 단축 와
# DP 과정 발상도 개오진다 진짜.
# 계산 실수 오지게 나옴 디버깅도 힘드네 ㅋㅋ
import sys


def make_round(n):
    if n >= int(n) + 0.5:
        return int(n) + 1
    else:
        return int(n)


def calPsum(L):
    global pSum, ppSum
    n = len(L)
    pSum.append(L[0])
    ppSum.append(L[0] ** 2)
    for i in range(1, n):
        pSum.append(pSum[i] + L[i])
        ppSum.append(ppSum[i] + L[i] ** 2)


def minQuan(start, end):
    global L, pSum, ppSum
    # 평균을 구하자
    A = pSum[end + 1] - pSum[start]
    AA = ppSum[end + 1] - ppSum[start]
    average = make_round((A) / (end - start + 1))
    # A^2 + 2mA + m^2(b-a+1)
    q = AA - 2 * average * A + (average ** 2) * (end - start + 1)
    return q


def DP(begin, part):
    global n, L, Cache
    if begin == n:
        return 0
    if part == 0:
        return sys.maxsize
    if Cache.get((begin, part), -1) != -1:
        return Cache[(begin, part)]
    ret = sys.maxsize
    for i in range(n - begin):
        ret = min(ret, minQuan(begin, begin + i) + DP(begin + i + 1, part - 1))
    Cache[(begin, part)] = ret
    return ret


read = sys.stdin.readline
T = int(read())
ans = []
for _ in range(T):
    n, s = map(int, read().split())
    L = sorted(list(map(int, read().split())))
    pSum = [0]
    ppSum = [0]
    calPsum(L)
    Cache = dict()  # (from,parts)
    ans.append(DP(0, s))
for a in ans:
    sys.stdout.write("{}\n".format(a))
