# 기둥 설치가능한지 확인
# pass 가능 1 불가능 0 반환
def row_check(x, y, result):
    if y == 0:
        return 1
    for r in result:
        i, j, a = r[0], r[1], r[2]
        if i == x and j == y - 1 and a == 0:
            return 1
        if i == x - 1 and j == y and a == 1:
            return 1
        if i == x and j == y and a == 1:
            return 1


def col_check(x, y, result):
    # 보 설치 가능한지 확인
    # 가능 1 불가능 0
    # 양옆에 보있는지 확인하는 flag
    flag1, flag2 = 0, 0
    for r in result:
        i, j, a = r[0], r[1], r[2]
        if i == x and j == y - 1 and a == 0:
            return 1
        if i == x + 1 and j == y - 1 and a == 0:
            return 1
        if i == x - 1 and j == y and a == 1:
            flag1 = 1
        if i == x + 1 and j == y and a == 1:
            flag2 = 1
    if flag1 == 1 and flag2 == 1:
        return 1


def solution(n, bulid):
    result = []
    for b in bulid:
        x, y, a, b = b[0], b[1], b[2], b[3]
        if b == 0:  # 삭제
            if a == 0:  # 기둥삭제
                copy = []
                flag = 1
                for r in result:
                    if r[0] == x and r[1] == y and r[2] == 0:
                        continue
                    copy.append(r)
                for r in copy:
                    x2, y2, a2 = r[0], r[1], r[2]
                    if x2 == x and y2 == y + 1 and a2 == 0:
                        if row_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                    elif x2 == x - 1 and y2 == y + 1 and a2 == 1:
                        if col_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                    elif x2 == x and y2 == y + 1 and a2 == 1:
                        if col_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                if flag == 1:  # 무시 안하니 지운값을 result로
                    result = copy
            elif a == 1:  # 보삭제
                copy = []
                flag = 1
                for r in result:
                    if r[0] == x and r[1] == y and r[2] == 1:
                        continue
                    copy.append(r)
                for r in copy:
                    x2, y2, a2 = r[0], r[1], r[2]
                    if x2 == x and y2 == y and a2 == 0:
                        if row_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                    elif x2 == x + 1 and y2 == y and a2 == 0:
                        if row_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                    elif x2 == x - 1 and y2 == y and a2 == 1:
                        if col_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                    elif x2 == x + 1 and y2 == y and a2 == 1:
                        if col_check(x2, y2, copy) != 1:
                            flag = 0
                            break
                if flag == 1:
                    result = copy
        elif b == 1:  # 설치
            if a == 0:  # 기둥
                if row_check(x, y, result) == 1:
                    result.append([x, y, a])
            elif a == 1:  # 보
                if col_check(x, y, result) == 1:
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
