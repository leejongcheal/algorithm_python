import sys

a = int(sys.stdin.readline().rstrip())
sum = 0
for i in range(a+1):
    if i % 2 ==0:
        sum += i
print(sum)