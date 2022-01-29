def row_check(x, y, result):
    if y == 0:
        return 1
    for r in result:
        i, j, a = r[0], r[1], r[2]
        if i == x and j == y and a == 1:
            return 1
        if i == x - 1 and j == y and a == 1:
            return 1
        if i == x and j == y - 1 and a == 0:
            return 1
    return 0


def bottom_check(x, y, result):
    b0, b1 = 0, 0
    for r in result:
        i, j, a = r[0], r[1], r[2]
        if i == x and j == y - 1 and a == 0:
            return 1
        if i == x + 1 and j == y - 1 and a == 0:
            return 1
        if i == x - 1 and j == y and a == 1:
            b0 = 1
        if i == x + 1 and j == y and a == 1:
            b1 = 1
    if b0 == 1 and b1 == 1:
        return 1
    else:
        return 0

def check_L(L):
    for l in L:
        x, y, a = l[0], l[1], l[2]
        if a == 0:
            if row_check(x, y, L) == 0:
                return 0
        elif a == 1:
            if bottom_check(x, y, L) == 0:
                return 0
    return 1



def return_remove(result, x, y, a):
    remove_result = []
    for r in result:
        i, j, ra = r[0], r[1], r[2]
        if i == x and j == y and ra == a:
            continue
        else:
            remove_result.append([i, j, ra])
    return remove_result


def solution(n, bulid):
    result = []
    for bu in bulid:
        x, y, a, b = bu[0], bu[1], bu[2], bu[3]
        if b == 0:
            # 삭제와 기둥
            if a == 0:
                L = return_remove(result, x, y, a)
                if check_L(L):
                    result = L
            # 삭제와 바닥
            elif a == 1:
                L = return_remove(result, x, y, a)
                if check_L(L):
                    result = L
        elif b == 1:
            # 설치와 기둥
            if a == 0:
                if row_check(x, y, result):
                    result.append([x, y, a])
            # 설치와 바닥
            elif a == 1:
                if bottom_check(x, y, result):
                    result.append([x, y, a])
    result.sort()
    return result


# 입력및 초기화 부분
N, K = map(int, input().split())
bulid = []
for _ in range(K):
    # x,y,a,b
    bulid.append(list(map(int, input().split())))
# x y a 배열 넣어주기
result = solution(N, bulid)
print(result)
