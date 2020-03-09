# 전에꺼랑 다르게 수열 2개 가지고 푸는 문제 따라서 그냥 A+B = C 로 해서 C에서 전처럼 풀려 했으나
# A,B의 앞부분에서 작은걸로 선택하는게 더 길어질것은 명백함 -> 따라서 A,B중 작은것을 뽑아내서 C를 만들고나서 풀기
# 책은  jlis(a,b) = max(jlis(a+1,b),jlis(a,b+1)) + 1처럼 풀이함
# 그럼 굳이 C라는 메모리사용과 조합하는 시간을 아낄수 있다!
# 와 근데 저렇게 풀면 10 20 30 1 2/ 10 20 30 -> 1 2 30 이 나와 틀림 어떻게 할까
# 일단 A,B에 대해서 jls을 구한다음에 겹치는 수만큼만 뺸값을 답으로 하면 이상하게 답이나옴
# 일단 이문제는 이렇게 풀어보고 나중에는 DP로 제대로 이해해서 풀어볼것_ 너무어렵다 진짜
# 런타임에러가 뜨는데 이경우는 -2147483648 같은 아주작은값이 들어가는경우에 문제가 생김 아 너무하네 진짜
# 반례 194 347
import sys


def lower_bound(key, S):
    start = 1
    end = start + len(S) - 1
    while end - start > 0:
        mid = (end + start) // 2
        if key > S[mid]:
            start = mid + 1
        elif key < S[mid]:
            end = mid
        else:
            return mid
    return end


def solve():
    global A, B, n, S_a, S_b, cnt_a, cnt_b
    for i in range(cnt_a):
        S_appeend(A[i], S_a)
    for i in range(cnt_b):
        S_appeend(B[i], S_b)


def S_appeend(key, S):
    if key > S[-1]:
        S.append(key)
    elif key == S[-1]:
        return
    else:
        S[lower_bound(key, S)] = key


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    cnt_a, cnt_b = map(int, read().split())
    n = cnt_a + cnt_b
    A = list(map(int, read().split()))
    B = list(map(int, read().split()))
    S_a = [-sys.maxsize]
    S_b = [-sys.maxsize]
    solve()
    S = set(S_a) | set(S_b)
    print(S)
    print(len(S) - 1)
