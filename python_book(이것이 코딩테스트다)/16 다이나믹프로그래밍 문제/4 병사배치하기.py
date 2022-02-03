"""
이진탐색을 이용한 nlogn 풀이 LIS
솔직히 직관적으로 풀기힘든 방법이라고 생각함 유형암기아니면 못할듯?
"""
# from bisect import bisect_left, bisect_right
# N = int(input())
# L = list(map(int, input().split()))
# L = L[::-1]
# result = [L[0]]
# for i in range(1,N):
#     index = bisect_left(result, L[i])
#     if index >= len(result):
#         result.append(L[i])
#     else:
#         result[index] = L[i]
# print(N - len(result))
#

N = int(input())
L = list(map(int, input().split()))
L = L[::-1]
DP = [1]*N
for i in range(1, N):
    for j in range(i):
        if L[i] > L[j]:
            DP[i] = max(DP[i], DP[j] + 1)
""" 
    굳이 왜저렇게 풀었을까 ㅜㅜ 경계값실수 j부분이 1 ~ i가 들어가야 L[i - j]가 0 ~ i - 1값이 들어가는데
    경계를 ragne(i) -> ragne(1, i+1) 로 해야함
"""
# for i in range(1, N):
#     for j in range(i):
#         if L[i] > L[i - j]:
#             DP[i] = max(DP[i], DP[i - j] + 1)
print(N - max(DP))
