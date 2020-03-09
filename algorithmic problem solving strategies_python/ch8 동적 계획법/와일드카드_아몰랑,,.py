import sys


def solve(s, w):
    global S, W, dic
    if dic.get((s, w), -1) != -1:
        return dic[(s, w)]
    if s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        dic[(s,w)] = solve(s+1,w+1)
        return dic[(s,w)]
    # 대응이 끝난 경우 1.대응이 불가능 2.문자열 끝까지 와서 대응 3. *출현
    if w == len(W):  # 1,2
        if s == len(S):  # 2
            dic[(s, w)] = 1
        else:  #  1
            dic[(s, w)] = 0
        return dic[(s, w)]
    if W[w] == '*':  # 3
        if solve(s,w+1) or (s< len(S) and solve(s+1,w)):
            dic[(s,w)] = 1
            return 1
    dic[(s,w)] = 0
    return 0


read = sys.stdin.readline
T = int(read())
res = []
for _ in range(T):
    W = read().strip()
    n = int(read())
    for _ in range(n):
        S = read().strip()
        dic = dict()
        flag = solve(0, 0)
        if flag == 1:
            res.append(S)
res.sort()
for c in res:
    print(c)
