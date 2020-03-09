R, C = map(int, input().split())
b = [list(input()) for _ in range(R)]
t = {}


def f(x, y, v):
    k = x, y, str(v)
    if k in t:  # 어떤 한경로에 대해서 같은점인 경우는 하나로 보고 전의값 가져와서 써버림
        return t[k]
    if x < 0 or y < 0 or x >= R or y >= C or b[x][y] in v:
        return 0
    n = v + [b[x][y]]  # 경로를 문자열 상태로 계속 가지고 넘김
    t[k] = max(f(x + 1, y, n), f(x, y + 1, n), f(x - 1, y, n), f(x, y - 1, n)) + 1
    return t[k]


print(f(0, 0, []))
for i in t:
    print(i)
