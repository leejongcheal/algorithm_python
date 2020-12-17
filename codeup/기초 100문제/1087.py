import sys
a = int(sys.stdin.readline().rstrip())
sum = 0
for i in range(a+1):
    sum += i
    if sum >= a:
        break
print(sum)