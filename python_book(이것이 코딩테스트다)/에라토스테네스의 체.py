""" 소수 판별을 위한 알고리즘
    1. 2부터 N 까지의 모든 자연수를 나열한다
    2. 남은 수중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
    3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거 하지않는다)
    4. 더 이상 반복할 수 없을때까지 2번과 3번의 과정을 반복한다.
    시간복잡도  O(Nlog(logN))
    오히려 공간복잡도가 걸려서 보통 1,000,000 이내로 주어지는 경우 사용
"""

import math

n = 1000
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")
