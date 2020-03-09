# 일단 크기가 커서 nlogn으로 풀어야함
# 뒤의값부터 찾아서 넣고 뒤집어서 출력
import sys
from collections import deque

read = sys.stdin.readline
ans = []
for _ in range(int(read())):
    res = deque()
    n = int(read())
    shift = list(map(int, read().split()))
    sortedL = [i for i in range(1,n+1)]
    for i in shift[::-1]:
        print(i, len(sortedL))
        res.appendleft(sortedL.pop(-i-1))
    ans.append(res)
for a in ans:
    sys.stdout.write("{}\n".format(" ".join(map(str,a))))

