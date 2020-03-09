# 시간복잡도가 nlong인 풀이법
# 책보고 품 이분탐색이 logn의 시간복잡도를 가짐 이를 이용해서 푼 방법-> 이걸 어떻게 발상하냐 ㅋㅋ
# https://jason9319.tistory.com/113 참고 와 대단...
# lower_bound 함수 배우기 찾고자 하는 값 이상이 처음 나타나는 위치
import sys


def lower_bound(n, key):
    global S
    start = 1
    end = start + n - 1
    while end - start > 0:
        mid = (end+start)//2
        if key > S[mid]:
            start = mid + 1
        elif key < S[mid]:
            end = mid
        else:
            return mid
    return end


def solve():
    global L, S, n
    for i in range(n):
        if L[i] > S[-1]:
            S.append(L[i])
        elif L[i] == S[-1]:
            continue
        else:
            S[lower_bound(len(S),L[i])] = L[i]


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = list(map(int, read().split()))
    S = [-1]
    solve()
    print(S)
    print(len(S)-1)
