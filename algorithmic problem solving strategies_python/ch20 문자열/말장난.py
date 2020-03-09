# 시간 초과뜸 접미사 배열을 쓰라는데 이해안감 ㅋㅋ 알고스팟이 병신인건가 ㅋㅋ
import sys
T = int(input())
read = sys.stdin.readline
for _ in range(T):
    k = int(read())
    s = read()
    subset = set()
    for i in range(1,len(s)):
        for j in range(len(s)-i):
            subset.add(s[j:j+i])
    res = 0
    for c in subset:
        if s.count(c) >= k:
            res = max(res,len(c))
    print(res)


