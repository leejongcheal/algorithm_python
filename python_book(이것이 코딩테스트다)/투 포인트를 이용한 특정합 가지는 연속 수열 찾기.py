"""
투 포인터 알고리즘 : 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
특정합을 가지는 연속 수열 찾는 경우
전제조건 양수를 가진 수열
1. 시작점 start 와 끝점 end 가 첫 뻔째 원소의 인덱스를 기리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작으면 end 를 1 증가시킨다.
4. 현재 부분합이 M보다 크거나 같으면 start 를 1증가 시킨다.
5. 모든 경우를 확인할 떄 까지 2번부터 4번의 과정을 반복한다.

start 가 end 를 앞서는 경우에 대해서 고민을 했는데 start가 end보다 앞에 있다면 값은 0 또는 음수의 값을
가져서 부분합 < m에 걸려서 end >= start 상태를 유지하게 된다.
+ end는 더하는 값이고 start는 빼는 값
"""
# 데이터 갯수, 찾고자 하는 부분합
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0
for start in range(n):
    # 부분합 < m 인경우는 end += 1
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합 >= m 인경우 start += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
