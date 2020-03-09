# 입력의 예시가 없어서 그냥 구현 하는걸로 만족
# 재귀를 사용할때 기저 사례 선택
# 1. 원하는 글자랑 틀릴떄 실패
# 2. 글자의 길이가 1이고 시작지점에 맞을때 성공 -> 맞는데 길이가 끝인 경우로 일반화
# 3. 글자의 끝까지 왔는데 맞을 경우 성공
# 알고스팟에선 틀림 인풋이 AAAAAAAAAB이고 맵이 AAA~~~~AAAB인 경우 시간초과 이런거 처리는 어떻게 할까....
# 메모제이션을 통한 해결!!!(캐시) ++ 문제마다 dic를 초기화 해줘야하는데 이런 기본적인 실수를 함 ㅜㅜ
import sys


def check_word(x, y, word, i):
    global L, dir, dic
    if L[x][y] != word[i]:
        return 0
    else:
        if len(word) - 1 == i:
            return 1
        else:
            if dic.get((x, y, i), -1) != -1:
                return dic[(x, y, i)]
            elif dic.get((x, y, i), -1) == -1:
                f = 0
                for c in dir:
                    if -1 < x + c[0] < 5 and -1 < y + c[1] < 5:
                        f = check_word(x + c[0], y + c[1], word, i + 1) or f
                dic[(x, y, i)] = f
                return dic[(x, y, i)]
            else:
                print("오류")


def solve(word):
    global flag
    flag = 0
    for x in range(5):
        for y in range(5):
            if check_word(x, y, word, 0) == 1:
                print(word + " YES")
                return
    print(word + " NO")


T = int(input())
read = sys.stdin.readline
dir = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
for _ in range(T):
    L = []
    for i in range(5):
        L.append(read())
    n = int(read())
    for _ in range(n):
        a = read().replace("\n", "")
        dic = dict()
        solve(a)

