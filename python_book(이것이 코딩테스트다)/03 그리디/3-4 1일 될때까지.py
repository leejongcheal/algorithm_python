n, k = map(int, input().split())
cnt = 0
while True:
    # 현재 나머지값을 n에 빼줘서 k의 배수로 만듬
    remainder = n % k
    cnt += remainder
    n -= remainder
    # n을 k로 나눠주고 나머지를 뺴주는 과정을 0이 될때까지 반복
    if n != 0:
        n //= k
        cnt += 1
    else:
        break
# 1까지가 목적인데 조건은 0으로 줬으니 count의 갯수를 하나 뺀다.
print(cnt - 1)