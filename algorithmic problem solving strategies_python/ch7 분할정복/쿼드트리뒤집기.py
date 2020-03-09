# 입력의 크기가 매우크기 떄문에 브루트포스 no -> 큰입력에도 돌아가는 알고리즘 or 작은 입력에서 돌아가는 알고리즘으로 최적화 생각
# 저장되는 형태가 재귀이니 압축 또는 해제하는 과정도 재귀로 한다.
# 1234 -> 3142 형태로 변환을 밑에서 부터 차례로 한다
# x 는 리스트로 4개 저장으로 일단 저장후 [1[1[]34]34] 이런식 재귀식으로 들어가서 바꾸면서 나오게 하기
# 다시 저장한 T가 [[]234]이런식도 있지만 [[12[]4]]이런 경우도 생각해야함 len(T)가 1임 이경우 떔에 시간좀 걸림
import sys
from collections import deque


# x인 경우 앞의 4개 요소 리스트로 묶어서 리스트와 끝 index 리턴(재귀적)
def ifx(i):
    global quadT
    L = []
    for cnt in range(4):
        i += 1
        if quadT[i] == 'x':
            t, i = ifx(i)
            L.append(t)
        else:
            L.append(quadT[i])
    return L, i


# 받은 리스트에 대해서 x+2301 str형식으로 리턴 이때 재귀적 호출 사용
def updown(L):
    global res
    i = 0
    for c in L:
        if type(c) == type([]):
            L[i] = updown(L[i])
            i += 1
        else:
            i += 1
    return 'x' + L[2] + L[3] + L[0] + L[1]


T = int(input())
read = sys.stdin.readline
for _ in range(T):
    quadT = read().replace("\n", "")
    q = deque()
    T = []
    i = 0
    res = ""
    while i < len(quadT):
        if quadT[i] == 'x':
            t, i = ifx(i)
            T.append(t)
        else:
            T.append(quadT[i])
        i += 1
    i = 0
    #print(T)
    if len(T) > 1 or type(T[0]) == type([]):
        for c in T:
            if type(c) == type([]):
                res += updown(c)
            else:
                res += c
    else:
        res += T[0]
    print(res)
