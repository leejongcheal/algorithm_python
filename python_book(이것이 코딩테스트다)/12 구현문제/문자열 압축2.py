S = input()
N = len(S)
L = []
result = int(1E9)
for k in range(1, N//2 + 1):
    res = ""
    pre = ""
    now = ""
    cnt = 0
    same_cnt = 1
    # cnt가 k개 일때 pre now 비교해서 res 만들기
    for i in range(0, N - (N%k)):
        cnt += 1
        now += S[i]
        if cnt == k and pre == "":
            pre = now
            res += now
            now = ""
            cnt = 0
        elif cnt == k and pre != "":
            if pre == now:
                same_cnt += 1
            else:
                if same_cnt > 1:
                    res += str(same_cnt) + now
                    same_cnt = 1
                    pre = now
                else:
                    res += now
                    pre = now
            now = ""
            cnt = 0
    # 끝나서 나온경우
    if same_cnt > 1:
        res += str(same_cnt)
    # 그냥 나머지는 더하면됨
    for i in range(N - (N%k), N):
        res += S[i]
    L.append(res)
    result = min(len(res), result)
print(L, result)