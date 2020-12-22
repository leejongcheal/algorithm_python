n, m, k = map(int, input().split())
L = list(map(int,input().split()))
L.sort()
first = L[n-1]
second = L[n-2]
result = 0
# fisrt k번과 second 더한것을 하나의 set으로 보았을때 더해야할 갯수
count = m // (k+1)
# set으로 안묶이는 fisrt를 더해야할 갯수
remainder = m %(k+1)
# 위의 계산값을 토대로 결과 구하기
result += count*(first*k + second)
result += remainder*first
print(result)