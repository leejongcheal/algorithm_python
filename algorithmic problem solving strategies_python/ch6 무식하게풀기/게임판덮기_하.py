# 일단 블록의 모습으로 놓았을때 표현을 어떻게할까...
# 흰블록의 갯수가 3의 배수여야함 2*3/ 3*2 의 블록을 채우는 방법은 각각 2가지임!
# 중복의 갯수를 센다 -> 강제된 순서를 가지게한다
# 젤위의 왼쪽부터 채운다 -> 자기위치의 위+왼쪽은 다 채워져 있다!
# 이중for문 break 두번 채워서 나오는거 까먹........이것땜에 시간 많이 날림
import sys


def cover(mapL):
    global n, m, res, dir
    flag = 1
    for x in range(n-1, -1, -1):
        for y in range(m):
            if mapL[x][y] == '.':
                flag = 0
                break
        if flag == 0:
            break
    # 빈게 없는 경우니까!
    if flag == 1:
        res += 1
        return
    for l in dir:
        flag = 1
        for c in l:
            if 0 <= x + c[0] < n and 0 <= y + c[1] < m and mapL[x + c[0]][y + c[1]] == '.':
                continue
            else:
                flag = 0
                break
        if flag == 1:
            for c in l:
                mapL[x + c[0]][y + c[1]] = '#'
            cover(mapL)
            for c in l:
                mapL[x + c[0]][y + c[1]] = '.'


T = int(input())
read = sys.stdin.readline
dir = [[(0, 0), (0, 1), (-1, 1)], [(0, 0), (-1, 0), (-1, 1)], [(0, 0), (-1, -1), (-1, 0)], [(0, 0), (0, 1), (-1, 0)]]
for _ in range(T):
    n, m = map(int, read().split())
    L = []
    white_m = 0
    for _ in range(n):
        L.append(list(read()))
    for i in range(n):
        white_m += L[i].count('.')
    if white_m % 3 == 0:
        res = 0
        # 일단 흰색의 갯수 찾기
        cover(L)
        print(res)
    else:
        print(0)
