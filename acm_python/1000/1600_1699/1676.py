N = int(input())
dic = {2: 0, 5: 0}
for i in range(1, N + 1):
    n = i
    while n % 5 == 0:
        dic[5] += 1
        n //= 5
result = dic[5]
print(result)

# 문제해설 결국에 10이 몇개생기냐를 세는 것인데 10 = 2 * 5 즉 2,5의 갯수를 세서 최소값을 출력
#  근데 사실상 5는 2보다 많이 나올수 가 없어서 5만 세면됨
