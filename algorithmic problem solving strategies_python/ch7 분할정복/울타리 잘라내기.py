# 일단 브루트 포스는 안됨 N^2인데 2만개의 입력
# 따라서 분할정복으로 풀이 -> 세부사항은 p199확인
# 처음에는 1 왼쪽만 2오른쪽만 3걸쳐서 에서 3에 대해서 모든부분(0~n-1) 확인함 -> N^2의 복잡도
# 주어진 범위에 대해서만 3을 함으로 고침 -> 이게 분할정복이지 !
# while문 범위 실수해서 오답 처리뜸 ㅜㅜ
# while left < tmp1 and tmp2 < right: -> while left <= tmp1 and tmp2 <= right:
# 첫번쨰로 하면 tmp1가 left인데 tmp2는 더돌수 있는경우를 무시하기 떄문에 ㅜㅜ
import sys


def solve(left, right):
    global L
    # 기저사례 1의 칸만 있을때
    if left == right:
        return L[left]
    half = (left + right) // 2
    area1 = solve(left, half)
    area2 = solve(half + 1, right)
    tmp1 = half  # 왼쪽 1칸포함
    tmp2 = half + 1  # 오른쪽 1칸포함
    h = min(L[tmp1], L[tmp2])
    width = 2
    area = h * width
    while left <= tmp1 and tmp2 <= right:
        width += 1
        if tmp1 > left and tmp2 < right:  # 왼쪽,오른쪽 둘다 확장 가능할때
            if L[tmp1 - 1] < L[tmp2 + 1]:  # 오른쪽으로 확장
                tmp2 += 1
                if h > L[tmp2]:
                    h = L[tmp2]
            else:  # 왼쪽으로 확장
                tmp1 -= 1
                if h > L[tmp1]:
                    h = L[tmp1]
        elif tmp1 > left:  # 왼쪽 확장만 가능할때
            tmp1 -= 1
            if h > L[tmp1]:
                h = L[tmp1]
        elif tmp2 < right:  # 오른쪽 확장만 가능할때
            tmp2 += 1
            if h > L[tmp2]:
                h = L[tmp2]
        else:
            break
        area = max(area, h * width)
    return max(area1, area2, area)


T = int(input())
read = sys.stdin.readline
for _ in range(T):
    n = int(read())
    L = list(map(int, read().split()))
    print(solve(0, n - 1))
