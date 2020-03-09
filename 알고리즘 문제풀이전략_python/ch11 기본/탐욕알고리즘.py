# 탐욕 알고리즘 문제 
# S(0) = 0 으로 확정후에 나머지는 max로두고 채워가는 문제
import sys
# 변형해서 품 아 졸라 귀찮네 리얼
m = int(input("최대 메모리: "))
S =[-1]* (m+1)
S[0] = 0
A = []
n = int(input("앱의 갯수 :"))
nameList = sys.stdin.read().splitlines()
print("----------------",n)
for i in range(n):
    x,y = map(int, nameList[i].split())
    A.append([x,y])

for i in range(0,m+1):
    if S[i] != -1:
        for a in A:
            if i + a[1] <= m:
                if S[i+a[1]] == -1:
                    S[i+a[1]] = S[i] + a[0]
                elif S[i] + a[0] < S[i+a[1]]:
                    S[i+a[1]] = S[i] + a[0]
print(S)
print(S[m])
