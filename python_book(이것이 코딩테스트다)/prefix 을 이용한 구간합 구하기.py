"""
prefix를 이용한 구간합 구하기
알고리즘
1. N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L - 1] 이다.
"""
n = 5
data = [10, 20, 30, 40, 50]
# 접두사합 구하기
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])