k = int(input())
sign = list(input().split())
# max
max = []
min = []
for i in range(9,8-k,-1):
    max.append(str(i))
for i in range(k+1):
    min.append(str(i))

count = 1
while count == 1:
    count = 0
    for idx in range(k):
        if sign[idx] == "<" and max[idx] > max[idx + 1]:
            max[idx], max[idx+1] = max[idx+1], max[idx]
            count = 1
        elif sign[idx] == ">" and max[idx] < max[idx + 1]:
            max[idx], max[idx+1] = max[idx+1], max[idx]
            count = 1
count = 1
while count == 1:
    count = 0
    for idx in range(k):
        if sign[idx] == "<" and min[idx] > min[idx + 1]:
            min[idx], min[idx+1] = min[idx+1], min[idx]
            count = 1
        elif sign[idx] == ">" and min[idx] < min[idx + 1]:
            min[idx], min[idx+1] = min[idx+1], min[idx]
            count = 1
print("".join(max))
print("".join(min))


