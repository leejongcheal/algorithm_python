import sys

a = int(sys.stdin.readline().rstrip())
sum = 0
c = 0
for i in range(a):
    sum += i
    if sum >= a:
        c = i
        break
print(c)