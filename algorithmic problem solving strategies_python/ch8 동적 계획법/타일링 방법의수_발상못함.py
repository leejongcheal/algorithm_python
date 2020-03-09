# 일단 저번에 본적있긴했음 그래서 발상할려 했는데 안되네
# 나느 f(n) = f(n-1) + 2*f(n-2) - 1(가로로 쭉있는경우 겹침) 해서 풀려 했는데 안됨
# ㅣ(f(n-1)) + =(f(n-2)) 발상을 못함 ㅜㅜ 일단 메모리제이션인건 알겠음
import sys


def solve(n):
    global dic
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dic.get(n,-1) != -1:
        return dic[n]
    dic[n] = (solve(n-1) + solve(n-2)) % 1000000007
    return dic[n]


read = sys.stdin.readline
T = int(read())
ans = []
dic = dict()
for _ in range(T):
    n = int(read())
    ans.append(solve(n))
for a in ans:
    sys.stdout.write("{}\n".format(a))
