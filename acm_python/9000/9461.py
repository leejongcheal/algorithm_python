dic = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9}
def DP(n):
    if dic.get(n,-1) != -1:
        return dic[n]
    else:
        dic[n] = DP(n-1)+DP(n-5)
        return dic[n]


n = int(input())
for _ in range(n):
    print(DP(int(input())))
