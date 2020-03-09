from math import *
from collections import deque


def solve(n):
    cnt = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if gcd(i,j) == 1:
                print("찾은 기약 분수 : %d/%d" %(i,j))
                cnt += 1
    print("찾은 기약 분수 : %d/%d" %(1,1))
    cnt += 1
    print("\n총 %d개의 기약 분수가 존재합니다\n" % cnt)


T = int(input())
L = deque()
for _ in range(T):
    L.append(int(input()))
for _ in range(T):
    solve(L.popleft())
