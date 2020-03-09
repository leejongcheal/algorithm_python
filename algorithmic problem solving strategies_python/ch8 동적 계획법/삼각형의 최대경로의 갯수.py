# 처음에 삽질좀 함 --- 맨밑칸으로 올수있는 경로의수를 점화식으로 세울려고 하다가 도저히 몰라서 다른사람 풀이봄
# n은 최대 100개 테스트갯수 C는 1~50개 2중 반복문이니 시간복잡도는 총 (n^2)*C
# 삼각형이니 (100^2/2)*50 = 25만개 5초동안 25만개 충분
# 따라서 n^2 사용가능
# DP를 떠올리는 힌트 1) 경로의수 2)원래문제가 DP이니 그리고 위의 생각과 더불어 풀었어야함
import sys


def solve():
    global n, L, p
    p[0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                L[i][j] += L[i - 1][j]
                p[i][j] = p[i - 1][j]
            elif j == i:
                L[i][j] += L[i - 1][j - 1]
                p[i][j] = p[i - 1][j - 1]
            else:
                if L[i - 1][j] > L[i - 1][j - 1]:
                    L[i][j] += L[i - 1][j]
                    p[i][j] = p[i - 1][j]
                elif L[i - 1][j] < L[i - 1][j - 1]:
                    L[i][j] += L[i - 1][j - 1]
                    p[i][j] = p[i - 1][j - 1]
                else:  # 같은 경우니깐 어느경로로 와도 값은 똑같지만 경로는 다름 따라서 더해줌
                    L[i][j] += L[i - 1][j]
                    p[i][j] = (p[i - 1][j] + p[i - 1][j - 1])
    Max = max(L[n-1])
    res = 0
    for j in range(n):
        if L[n-1][j] == Max:
            res += p[n-1][j]
    return res


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = []
    p = []
    dic = dict()
    for i in range(n):
        L.append(list(map(int, read().split())))
        p.append([0] * (i + 1))
    print(solve())
