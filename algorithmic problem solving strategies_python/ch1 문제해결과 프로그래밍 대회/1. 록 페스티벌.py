import sys
input = sys.stdin.readline
for test_case in range(int(input())):
    N, L = map(int, input().split())
    day = list(map(int, input().split()))
    Min = int(1e10)
    for i in range(N-L + 1):
        temp = sum(day[i:i+L])
        Min = min(Min, temp / L)
        for j in range(L+1, N + 1 - i):
            temp += day[i + j - 1]
            Min = min(Min, temp / j)
    print(Min)


# 완전탐색인데 시간복잡도 잘못계산해서 DP 문제인가 고민함
# C 100 N 1000 L 1000으로 치고 최악의 경우 생각
# 100 *(1000 + 999 + ...1) ~= 100*1000*500 = 5천만 + 2초이니 4천만정도 친다할때 애매하게 될듯?